import flet as ft 
from thefuzz import fuzz
from wonderwords import RandomWord

def main(page: ft.Page):
    page.title = "Pydle"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER


    vowels = ['a','e','i','o','u']
    answer = RandomWord().word(word_min_length=5, word_max_length = 5).lower()
    #answer = "python"
    #^^^ debug value
    give_up = 0
    answer_reveal = f"The answer was: {answer.capitalize()}"
    correct_guess = 0
    #hint_count = 1
    #intro = ft.Text("Hello World!", size = 30, color = "pink600")

    def check_answer(e):
        #answer_score.value = "i was submitted!"
        m_score = fuzz.partial_ratio(answer, user_input.value.lower())
        give_up = answer_score.value is not None and answer_reveal in answer_score.value
        if m_score == 100 and not give_up:
            #answer_score.value = f"Correct! The answer was: {answer}"
            answer_score.value = "Correct! " + answer_reveal.upper()
            correct_guess = 1
        else:
            if not give_up:
                answer_score.value = f"You are {m_score}% correct!"
        page.update()

    def give_hint(e):
        if answer_hint.value == "":
            first_letter : string = answer[0]
            last_letter : string = answer[-1]
            answer_hint.value = f"This word starts with a \"{first_letter.upper()}\" and ends with a \"{last_letter.upper()}\""
            hint_count = 0
        elif "This word starts" in answer_hint.value:
            answer_vowels = []
            for letter in answer:
                if (letter in vowels) and not(letter in answer_vowels):
                    answer_vowels.append(letter)
            answer_hint.value = answer_hint.value, f"It also contains these vowels: {answer_vowels}"

        #answer_hint.value = "massive ass fart"
        #^^^ sleep deprived debug comment 
        page.update()

    def give_up_event(e):
        #give_up = 1
        if not correct_guess:
            answer_score.value = answer_reveal
        page.update()
        
    def new_game(e):
        #add an animation to title
        #change color or gradient or size or something in resoonse to new_game_button
        #global answer
        user_input.value = ""
        answer_score.value = ""
        #answer_hint = ""
        answer_hint.value = ""
        #answer = RandomWord().word().lower()
        give_up = 0
        correct_guess = 0
        answer_reveal = ""
        page.update()

    title_card = ft.Text(value="Pydle", size= 70)

    user_input = ft.TextField(value = "", hint_text = "What's today's answer?", text_align = ft.TextAlign.CENTER, on_submit=check_answer)
    
    answer_score = ft.Text()

    hint_button = ft.TextButton(text = "Hint", on_click=give_hint)
    answer_hint = ft.Text(value = "")
    
    give_up_button = ft.TextButton(text = "Give Up", on_click=give_up_event)

    new_game_button = ft.TextButton(text="New Game", on_click=new_game)

    page.add(ft.Column
            ([
            title_card,
            user_input,
            #ft.Row([ hint_button, give_up_button, new_game_button ]),
            ft.Row([ hint_button, give_up_button], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([answer_hint], alignment = ft.MainAxisAlignment.CENTER),
            ft.Row([answer_score], alignment = ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment = ft.CrossAxisAlignment.CENTER
             #, expand=True
        )
    )
ft.app(target=main)

#things to do: 
    #1) fix reset button, doesn't do anything but clear text so fart
    #2) animate title for when text is reset
    #3) shows you which letters you got right instead of some seemingly random ass number lol
