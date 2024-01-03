import justpy as jp
import pandas as pd
import requests
from abc import ABC, abstractmethod


@abstractmethod
class Page(ABC):
    def serve(self):
        pass


class Home(Page):
    path = "/home"
    alternative_path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page", classes="text-4xl m-2")
        jp.Div(a=div, text=
        """
        lorem1f eifjei eijief iejfinr epsoee frfiejf iejdenef 
        eifeifef eijfiefne ijewinfeeewi eeijdiewfew ijewidew
        weifjewifjew weifewifew iewjfn ijwefinewfiwnf ewifnienfw
        wefewifew iwefjiewfe iwejfiewj iwejdfiew ewfjewif ewfewi
        """, classes="text-lg")
        return wp


jp.Route(Home.path, Home.serve)
jp.Route(Home.alternative_path, Home.serve)


def sum_up(widget, msg):
    sum = float(widget.input_1.value) + float(widget.input_2.value)
    widget.d.text = sum


def mouse_enter(widget, msg):
    widget.text = "Your Mouse Cursor has Entered"


def mouse_leave(widget, msg):
    widget.text = "Your Mouse Cursor has Left"


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="This is the About Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        lorem10 iodvioerfierr eirejfperfrifer eirjfiperfjjre 
        ierhfioerferjfprej eijfperfierfper ierjfiprefjer
        eifreifjerifr ierfperjifiperf ierjfiperpfjre eirjfperjf erijfperfnr
        eofr9wq9psqwodw ewjcoperogypujknigbu8gr8990y58065u0tn eiofjerifjreif43
        fir3ip34f7d7fgcgnjuuir i8gj4o5g73478wq erijferij3u2 32ej3fnigigef reif
        quswyd2tv2tkbkh gibngbi oyujko yj6j96y ihj4ru4bffbu uhhu3byv3b 
        """, classes="text-lg")
        return wp


jp.Route(About.path, About.serve)


class Dictionary(Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="Instant English Dictionary App", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the Definition of Any English Word", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_box = jp.Div(a=div, classes="m-2 p-2 text-lg h-40 border border-3 border-white h-20 bg-gray-200")

        input_box = jp.Input(a=input_div, placeholder="Type in any word here..", output_box=output_box,
                             classes="m-2 py-2 px-4 bg-blue-300 text-white border border-gray-200 rounded w-64 focus:outline-none focus:border-red-500 focus:bg-gray-400")

        input_box.on('input', cls.get_definition)

        # jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500",
        #           click=cls.get_definition, output_box=output_box, input_box=input_box)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        # This will give you the Tuple back:
        # widget.value is the User Input:
        # This is the word that is entered by the User:
        # req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        # data = req.json()
        # widget.output_box.text = " ".join(data['definition'])

        defined = Definition(widget.value).get()
        # Convert it into the String with the ' ':
        # This is the output for the Widget:
        widget.output_box.text = " ".join(defined)

    # @staticmethod
    # def api_definition(widget, msg):
    #     req = requests.get(f"http://127.0.0.1:8000/api?w={widget.page.input_box.value}")
    #     data = req.json()
    #     widget.page.output_box_2.text = " ".join(data['definition'])


# Reading the Data from here:
class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pd.read_csv('data.csv')
        return tuple(df.loc[df['word'] == self.term]['definition'])


class DefaultLayout(jp.QLayout):
    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)
        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        # Drawer need to be defined before it is being used:
        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True)
        # Set the Initial State of the Drawer to be False:
        drawer.value = False
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes_list = "p-2 m-2 text-lg text-blue-300 hover:text-blue-800"
        jp.A(a=qlist, text="Home", href="/home", classes=a_classes_list)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes_list)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes_list)
        jp.Br(a=qlist)
        # This is the Button that will trigger the Left Drawer which is the jp.QBtn:
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=self.move_drawer,
                drawer=drawer)
        #  Creating the QToolbarTitle here:
        # Since the Button and the Title have the Same Parent
        # It means to say that the Button will be Rendered before the Title:
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary App")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True


jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8081)
