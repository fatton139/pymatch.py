import partners


def match(gender, genderpref, height, heightpref, user_value):
    #Variables
    potential_partners = partners.Partners()
    partner_name = []
    partner_gender = []
    partner_gender_preference = []
    partner_height = []
    partner_height_preference = []
    partner_score = []
    partners_possible_list = []
    partners_equal_personality = []
    secondary_partner = []
    lowest_difference = 0
    #Counters
    partners_loaded = 0
    x = 0
    y = 0
    z = 0
    a = 0
    b = 0
    # print("There are", partners_loaded, "partners loaded")
    while potential_partners.available():
        partners_loaded += 1
        partner_name.append(potential_partners.get_name())
        partner_gender.append(potential_partners.get_gender())
        partner_gender_preference.append(potential_partners.get_sexual_pref())
        partner_height.append(potential_partners.get_height())
        partner_height_preference.append(potential_partners.get_height_pref())
        partner_score.append(potential_partners.get_personality_score())

    while x < partners_loaded:
        partner_list = [partner_name[x],
                        partner_gender[x],
                        partner_gender_preference[x],
                        partner_height[x],
                        partner_height_preference[x],
                        partner_score[x]]
        x += 1
        # print(partner_list)
        # print(x)
        if partner_list[1] == genderpref and partner_list[2] == gender:
            y += 1
            partners_possible = partner_list
            # print("match", y)
            # print("partner",x,"was matched")
            partners_possible_list.append(partners_possible)

    while len(partners_possible_list) > z:
        partner_value = partners_possible_list[z][5]
        difference = int(user_value) - int(partner_value)
        del partners_possible_list[z][5]
        partners_possible_list[z].append(abs(difference))
        # print(partners_possible[x])
        z += 1
    partners_possible_list.sort(key=lambda x: x[5])

    if len(partners_possible_list) > 0:
        lowest_difference = partners_possible_list[0][5]

    if len(partners_possible_list) >= 2:
        while len(partners_possible_list) > a:
            if partners_possible_list[a][5] == lowest_difference:
                partners_equal_personality.append(partners_possible_list[a])
            a += 1

    #print(partners_equal_personality)
    if len(partners_equal_personality) > 0:
        while len(partners_equal_personality) > b:
            if partners_equal_personality[b][3] == heightpref:
                secondary_partner.append(partners_equal_personality[b])
                #print("matched height preference",secondary_partner)
                return secondary_partner
            elif partners_equal_personality[b][4] == height:
                secondary_partner.append(partners_equal_personality[b])
                #print("matched partner's height preference",secondary_partner)
                return secondary_partner
            b += 1

    #print(partners_possible_list)
    return partners_possible_list


def input_validator(user_inputs, typeof_question):
    if typeof_question == "std":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 3:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) or 3 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 3:
                    return validated_input

    elif typeof_question == "personality":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 5:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) or 5 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 5:
                    return validated_input


def characteristics_question(question, answer1, answer2, answer3, answer4, answer5):
    if answer4 == 0 and answer5 == 0:
        input_val = input("\nWhat is your " + question + "?"
                          "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " + answer3 + "\n"
                          "Please enter your answer: ")
        validated_input = input_validator(input_val, "std")
        if question == "gender" or question == "gender preference":
            if validated_input == "1":
                return "male"
            elif validated_input == "2":
                return "female"
            elif validated_input == "3":
                return "other"
        elif question == "height" or question == "height preference":
            if validated_input == "1":
                return "tall"
            elif validated_input == "2":
                return "medium"
            elif validated_input == "3":
                return "short"
    else:
        if question == "q1":
            input_val = input("\nDo you find it easy to introduce yourself to other people?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " + answer3 + "\n4) " + answer4 +
                              "\n5) " + answer5 + "\nPlease enter your answer: ")
        if question == "q2":
            input_val = input("\nDo you usually initiate conversations?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " + answer3 + "\n4) " + answer4 +
                              "\n5) " + answer5 + "\nPlease enter your answer: ")
        if question == "q3":
            input_val = input("\nDo you often do something out of sheer curiosity?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " + answer3 + "\n4) " + answer4 +
                              "\n5) " + answer5 + "\nPlease enter your answer: ")
        if question == "q4":
            input_val = input("\nDo you prefer being out with a large group of "
                              "friends rather than spending time on your own?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " + answer3 + "\n4) " + answer4 +
                              "\n5) " + answer5 + "\nPlease enter your answer: ")
        validated_input = input_validator(input_val, "personality")
        return validated_input


def main():
    input_gender = 0
    input_gender_preference = 0
    input_height = 0
    input_height_preference = 0
    question_list = ["gender", "gender preference", "height", "height preference", "personality"]
    personality_question_list = ["q1", "q2", "q3", "q4"]
    personality_values = []
    x = 0
    y = 0

    print("Welcome to PyMatch")
    input_name = input("Please enter your name: ")
    print("\nHi", input_name + ".")

    while len(question_list) > x:
        question_type = question_list[x]
        x += 1
        if question_type == "gender" or question_type == "gender preference":
            answer1 = "male"
            answer2 = "female"
            answer3 = "other"
            answer4 = 0
            answer5 = 0
            if question_type == "gender":
                input_gender = characteristics_question(question_type, answer1, answer2, answer3, answer4,
                                                        answer5)
            if question_type == "gender preference":
                input_gender_preference = characteristics_question(question_type, answer1, answer2, answer3, answer4,
                                                                   answer5)

        if question_type == "height" or question_type == "height preference":
            answer1 = "tall"
            answer2 = "medium"
            answer3 = "short"
            answer4 = 0
            answer5 = 0
            if question_type == "height":
                input_height = characteristics_question(question_type, answer1, answer2, answer3, answer4,
                                                        answer5)
            if question_type == "height preference":
                input_height_preference = characteristics_question(question_type, answer1, answer2, answer3, answer4,
                                                                   answer5)

        if question_type == "personality":
            print("\nWe will now ask you some questions to try to determine your personality type.\n")
            while len(personality_question_list) > y:
                question_type = personality_question_list[y]
                y += 1
                answer1 = "Yes"
                answer2 = "Most of the time"
                answer3 = "Neutral"
                answer4 = "Some times"
                answer5 = "No"
                input_personality = characteristics_question(question_type, answer1, answer2, answer3, answer4,
                                                             answer5)
                personality_values.append(input_personality)

    total_inputs = [input_gender, input_gender_preference, input_height, input_height_preference, personality_values]
    user_pvalue = int(total_inputs[4][0]) + int(total_inputs[4][1]) + int(total_inputs[4][2]) + int(total_inputs[4][3])
    final_partner = match(total_inputs[0], total_inputs[1], total_inputs[2], total_inputs[3], user_pvalue*2)
    print("\nThank you for answering all the questions. We have found your best"
          "match from our database and hope that you enjoy getting to know"
          "each other. Your best match is:")
    if len(final_partner) == 0:
        print("none")
        return "none"
    else:
        print(final_partner[0][0])
        return final_partner[0][0]


main()
