from google import genai
from dotenv import load_dotenv
import os


# ========================================
# 1. load environment variables
# ========================================

load_dotenv()


# ========================================
# 2.get API key
# ========================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env files"
    )


# ==========================================
# 3. Create Gemini client
# ==========================================

client = genai.Client( 
    api_key=api_key 
) 


# ===========================================
# 4. Create chat session 
# ===========================================

chat = client.chats.create( 
    model="gemini-3.7-flash", 
    config={ 
        "system_instruction": """ 
        You are a helpful AI Assistant. 
 
        Answer questions clearly. 
        Use simple language. 
        Give examples when useful. 
        """ 
 
    } 
) 
 
 
print("=" * 50) 
print("             AI Assistant") 
print("=" * 50) 
 
print("Type 'exit' to stop.\n") 
 
 
while True: 
 
    user_input = input("You: ") 
 
    if user_input.lower() == "exit": 
        print("Assistant: Goodbye!") 
        break 
 
    try: 
 
        response = chat.send_message( 
            user_input 
        ) 


       # ============================================
       # response handling
       # ============================================ 
       
        print("\nAssistent:") 
        print(response.text) 
        print() 

 
    except Exception as e: 

        # =================================
        # error handling
        # =================================
 
        print("\nError occurred:") 
        print(e)
        print()

