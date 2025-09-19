class ChaiUtils:
    #decorated
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = "  water  ,  milk   , ginger  ,   honey  "

# obj = ChaiUtils()
# obj.clean_ingredients(raw)

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

#if you wants this method to be allowed without creating object then decorator comes into the picture
