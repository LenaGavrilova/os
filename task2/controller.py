#!/usr/bin/env python3
import os
import signal
import select

produced_count = 0


def sigusr_handler(signum, frame):
    global produced_count
    if signum == signal.SIGUSR1:
        print(f"Produced: {produced_count}")


def main():
    global produced_count

    signal.signal(signal.SIGUSR1, sigusr_handler)

    pipe1_0 = os.pipe()
    pipe0_2 = os.pipe()
    pipe2_0 = os.pipe()

    p1 = os.fork()

    if p1 == 0:
        os.close(pipe1_0[0])

        os.dup2(pipe1_0[1], 1)

        os.execl("./producer.py", "./producer.py")

    else:
        os.close(pipe1_0[1])

        p2 = os.fork()

        if p2 == 0:
            os.close(pipe0_2[1])
            os.close(pipe2_0[0])

            os.dup2(pipe0_2[0], 0)
            os.dup2(pipe2_0[1], 1)

            os.execl("/usr/bin/bc", "bc")

        else:
            os.close(pipe0_2[0])
            os.close(pipe2_0[1])

            results = []

            while True:
                reading_list,writing_list,exceptional_list = select.select([pipe1_0[0]], [], [], 1)
                if reading_list:
                    exp = os.read(pipe1_0[0], 10).decode("utf-8").strip()
                    if not exp:
                        break

                    os.write(pipe0_2[1],exp.encode("utf-8") + b"\n")
                    produced_count += 1
                    result = os.read(pipe2_0[0], 10).decode("utf-8").strip()
                    results.append((exp, result))

                for exp, result in results:
                    print(f"{exp} = {result}")
                results = []


if __name__ == "__main__":
    main()
