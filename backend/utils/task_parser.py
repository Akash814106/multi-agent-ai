def extract_tasks(plan_text):

    tasks = []

    lines = plan_text.split("\n")

    for line in lines:

        line = line.strip()

        # if line.startswith("1.") or \
        #     line.startswith("2.") or \
        #     line.startswith("3.") or \
        #     line.startswith("4.") or \
        #     line.startswith("5.") or \
        #     line.startswith("6.") :

        #     task = line.split(".",1)[1].strip()

        #     tasks.append(task)

        if "." in line and line.split(".",1)[0].isdigit():

            task = line.split(".",1)[1].strip()
            tasks.append(task)
    

    return tasks