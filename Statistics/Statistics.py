from StartCode import folder_statistics_path


class Statistics:
    main_speed = 0
    main_accuracy = 0
    main_symbols = 0

    def initialize_statistics_main_menu(main_stat, current_fields):
        global main_speed
        global main_accuracy
        global main_symbols
        main_speed = main_accuracy = main_symbols = 0

        Statistics.update_fields_main_menu("general", current_fields[1])
        Statistics.update_fields_main_menu("levels", current_fields[0])
        main_stat[0].setText(str(main_speed // 2))
        main_stat[1].setValue(int(main_accuracy // 2))
        main_stat[2].setText(str(main_symbols))
    
    def update_fields_main_menu(name_stat, current_fields,
                                folder_stat=folder_statistics_path):
        global main_speed
        global main_accuracy
        global main_symbols
        try:
            exercises_stat = folder_stat.joinpath(f"{name_stat}_stat.txt") \
                .read_text() \
                .split("\n")
        except OSError:
            return
        folder_stat.joinpath(f"{name_stat}_stat.txt") \
            .write_text("\n".join(exercises_stat))

        count = sum([int(line.split()[1]) for line in exercises_stat
                     if "count" in line])
        speeds = [int(line.split()[1]) for line in exercises_stat
                  if "speed" in line]
        accuracies = [int(line.split()[1]) for line in exercises_stat
                      if "accuracy" in line and line.split()[1] != "0"]
        curr_progress_symbols = sum(
            [int(line.split()[1]) for line in exercises_stat
             if "symbols" in line and line.split()[1] != "0"])
        count_speeds = count if name_stat == "general" else len(speeds)
        count_accuracies = count if name_stat == "general" else len(accuracies)
        curr_progress_speed = int(sum(speeds) // count_speeds) \
            if count_speeds != 0 else 0
        curr_progress_accuracy = int(sum(accuracies) / count_accuracies) \
            if count_accuracies != 0 else 0

        main_speed += curr_progress_speed
        main_accuracy += curr_progress_accuracy
        main_symbols += curr_progress_symbols

        current_fields[0].setText(str(curr_progress_speed))
        current_fields[1].setValue(curr_progress_accuracy)
        current_fields[2].setText(str(curr_progress_symbols))
        if name_stat == "levels":
            current_fields[3].setValue(
                int((curr_progress_speed + curr_progress_accuracy) // 10))

    def update_fields_levels_selection(levels_feilds,
                                       folder_stat=folder_statistics_path):
        try:
            levels_stat = folder_stat.joinpath("levels_stat.txt") \
                .read_text() \
                .split("\n")
        except OSError:
            return
        
        folder_stat.joinpath("levels_stat.txt") \
            .write_text("\n".join(levels_stat))
        for i in range(0, len(levels_stat), 6):
            levels_feilds[levels_stat[i]][0] \
                .setText(levels_stat[i + 2].split()[1])
            levels_feilds[levels_stat[i]][1] \
                .setValue(int(levels_stat[i + 3].split()[1]))

    def write_statistics_in_files(level_name, speed, right_letters_count, count,
                                  folder_stat=folder_statistics_path):
        current_file = "random_stat.txt" if level_name == "random" \
            else "levels_stat.txt"
        try:
            new_stat = folder_stat.joinpath(current_file).read_text() \
                .split("\n")
        except OSError:
            return

        for i, line in enumerate(new_stat):
            if line == "level {}".format(level_name):
                cur_speed = speed
                cur_accuracy = int(right_letters_count / count * 100)
                cur_symbols = count
                Statistics.write_statistics_in_stack(level_name, new_stat[1],
                                                     speed, cur_accuracy,
                                                     cur_symbols, folder_stat)
                
                if level_name != "random":
                    cur_speed = max(cur_speed,
                                    int(new_stat[i + 2].split()[1]))
                    cur_accuracy = max(cur_accuracy,
                                       int(new_stat[i + 3].split()[1]))
                    cur_symbols += int(new_stat[i + 4].split()[1])
                else:
                    Statistics.update_general_statistics_file(cur_speed,
                                                              cur_accuracy,
                                                              cur_symbols,
                                                              folder_stat)

                new_stat[i + 2] = "speed: {}".format(cur_speed)
                new_stat[i + 3] = "accuracy: {}".format(cur_accuracy)
                new_stat[i + 4] = "symbols: {}".format(cur_symbols)
                break
        folder_stat.joinpath(current_file).write_text("\n".join(new_stat))

    def write_statistics_in_stack(level_name, count, speed, accuracy, symbols,
                                  folder_stat=folder_statistics_path):
        try:
            stack = folder_stat.joinpath("stack_stat.txt").read_text() \
                .split("\n")
        except OSError:
            return
        
        stack.append(f"level {level_name}")
        stack.append(count)
        stack.append(f"speed {speed}")
        stack.append(f"accuracy {accuracy}")
        stack.append(f"symbols {symbols}")
        folder_stat.joinpath("stack_stat.txt").write_text("\n".join(stack))

    def update_general_statistics_file(new_speed, new_accuracy, new_symbols,
                                       folder_stat=folder_statistics_path):
        try:
            new_stat = folder_stat.joinpath("general_stat.txt").read_text() \
                .split("\n")
        except OSError:
            return

        new_stat[1] = "count: {}" \
            .format(int(new_stat[1].split()[1]) + 1)
        new_stat[2] = "speed: {}" \
            .format(int(new_stat[2].split()[1]) + new_speed)
        new_stat[3] = "accuracy: {}" \
            .format(int(new_stat[3].split()[1]) + new_accuracy)
        new_stat[4] = "symbols: {}" \
            .format(int(new_stat[4].split()[1]) + new_symbols)
        folder_stat.joinpath("general_stat.txt").write_text("\n".join(new_stat))
    
    def find_recruitment_dynam(folder_stat=folder_statistics_path):
        try:
            curr_stat = folder_stat.joinpath("stack_stat.txt").read_text() \
                .split("\n")
        except OSError:
            return
        
        levels = [level.split()[1] if level.split()[1] != "random" else "r"
                  for level in curr_stat if "level" in level]
        levels = [(i, level) for i, level in enumerate(levels)]
        speeds = [int(speed.split()[1]) for speed in curr_stat if "speed" in speed]
        accuracies = [int(accuracy.split()[1])
                      for accuracy in curr_stat if "accuracy" in accuracy]
        return levels, speeds, accuracies
    
    def clear_data(curr_file, folder_stat=folder_statistics_path):
        for file in folder_stat.iterdir():
            try:
                curr_stat = file.read_text().split("\n")
            except OSError:
                continue
            if file.name == curr_file:
                file.write_text("")
                continue
            curr_stat = [f"{line.split()[0]} 0" if "level" not in line and " " in line
                         else line
                         for line in curr_stat]
            file.write_text("\n".join(curr_stat))
