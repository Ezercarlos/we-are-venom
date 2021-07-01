import tkinter as tk


TEAL = "#E0F2F1"
LABEL_COLOR = "#3E2723"
SMALL_FONT_STYLE = ("Arial" , 16)
LARGE_FONT_STYLE = ("Arial" , 40 , "bold")
GREEN = "#E8F6F3"
DIGIT_FONT_STYLE = ("Arial" , 24 , "bold")
DEFAULT_FONT_STYLE = ("Arial" , 20)
GREEN_OFF = "#A2D9CE"
LIGHT_BLUE = "#7FB3D5"

class Calculator:
    def __innit__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()

        self.total_label , self.label = self.create_display_labels()

        self.digits = {
            7:(1 , 1) , 8:(1 , 2) , 9:(1 , 3) ,
            4:(2 , 1) , 5:(2 , 2) , 6:(2 , 3) ,
            1:(3 , 1) , 2:(3 , 2) , 3:(3 , 3) ,
            0:(4 , 2) , ".":(4 , 1)
        }

        self.operations = {
            "/": "\u00F7" , "*":"\u00D7" , "-":"-" , "+":"+"
        }

        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()

        self.create_operator_buttons()

    def create_display_labels(self):
        total_label = tk.label(self.display_frame , text=self.total_expression , anchor=tk.E ,
                                bg=TEAL , fg=LABEL_COLOR , padx=24 , font=SMALL_FONT_STYLE)
        total_label.pack(epand=True , fill="both")

        label = tk.label(self.display_frame , text=self.current_expression , anchor=tk.E ,
                                bg=TEAL , fg=LABEL_COLOR , padx=24 , font=LARGE_FONT_STYLE)
        label.pack(epand=True , fill="both")

        return total_label , label

    def create_display_frame(self):
        frame = tk.Frame(self.window , height=221 , bg=TEAL)
        frame.pack(expand=True , fill="both")
        return frame


    def create_digit_buttons(self):
        for digit , grid_value in self.digits.items():
            button = tk.Button(self.button_frame , text=str(digit) , bg=TEAL ,
                                fg=LABEL_COLOR , font=DIGIT_FONT_STYLE , borderwidth=0)
            button.grid(row=grid_value[0] , column=grid_value[1] , sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator , symbol in self.operations.items():
            button = tk.Button(self.buttons_frame , text=symbol ,
                                bg=GREEN_OFF , fg=LABEL_COLOR ,
                                font=DEFAULT_FONT_STYLE , borderwidth=0)
            button.grid(row=i , column=4 , sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame , text="C" ,
                                bg=GREEN_OFF , fg=LABEL_COLOR ,
                                font=DEFAULT_FONT_STYLE , borderwidth=0)
        button.grid(row=0 , column=1 , columnspan=2 , sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame , text="=" ,
                                bg=LIGHT_BLUE , fg=LABEL_COLOR ,
                                font=DEFAULT_FONT_STYLE , borderwidth=0)
        button.grid(row=4 , column=3 , columnspan=2 , sticky=tk.NSEW)


    def create_buttons_frame(self):
        frame =tk.Frame(self.window)
        frame.pack(expand=True , fill="both")
        return frame


    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    calc = Calculator
    calc.run()    

  