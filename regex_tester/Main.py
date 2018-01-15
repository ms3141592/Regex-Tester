import re
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


load_kivy_file = Builder.load_file("kivy_file.kv")


class TheScreen(BoxLayout):

    def user_input(self, text, reg):
        # set text return to original user input
        text_return = text

        try:
            # list of all regex found
            reg_list = re.findall(reg, text)
            # list of none regex
            none_reg_list = re.split(reg, text)
            # clear the text return after an expression is found
            text_return=''

            #
            for idx, item in enumerate(none_reg_list):
                text_return += item

                # change color of regex and add to text return
                if idx < len(none_reg_list)-1:
                    split_reg = list(reg_list[idx])
                    combine_reg = ''
                    for reg in split_reg:
                        # test for spaces and replace with uderscore if its part of regex
                        if reg is ' ':
                            combine_reg += '_'
                        else:
                            combine_reg += str(reg)
                    #
                    if combine_reg is not None:
                        text_return +=  '[color=#c06]{}[/color]'.format(combine_reg)
        except ValueError:
            pass
        except AttributeError:
            pass
        finally:

            return text_return


class MainApp(App):

    def build(self):
        return TheScreen()




if __name__ ==  '__main__':
    MainApp().run()