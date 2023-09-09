# Producing reports from user inputs and files.
def run_timing():
    run_list = []

    while True:
        
        run = input("How long does it take you to run 10 km(in mins): ")

        if run == "":
            break

        else:
            run = float(run)
            run_list.append(run)

    avg_time = sum(run_list)/len(run_list)
    print(run_list)
    print(f"The average run time is {avg_time} mins, over {len(run_list)} run(s).")

run_timing()