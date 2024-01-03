import justpy as jp
class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        div = jp.Div(a=wp, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="Instant Dictionary App", classes="text-4xl m-2")
        jp.Div(a=div, text="Get Definition of the Word", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="http://www.example.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "moon", "definition": ["A natural satellite of a planet.", "A month, particularly a lunar month (approximately 28 days).", 
        "To fuss over adoringly or with great affection.", "Deliberately show ones bare ass 
        (usually to an audience, or at a place, where this is not expected or deemed appropriate).", 
        "To be lost in phantasies or be carried away by some internal vision, having temorarily lost 
        (part of) contact to reality."]}
        """)
        return wp


# Setting the Route:
jp.Route("/api", Api.serve)

if __name__ == "__main__":
    jp.justpy()
