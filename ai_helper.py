import google.generativeai as genai
import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_creator_content(platform, topic):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if platform == "YouTube":
        prompt = f"""
        Act as an expert social media specialist. I need content for a YouTube video about: "{topic}".
        Please provide:
        1. 5 Clickable and engaging titles.
        2. A detailed, SEO-optimized video description.
        3. 15 relevant tags.
        Ensure the output is highly engaging and ready for publishing.
        """
    elif platform == "Instagram Carousel":
        prompt = f"""
        Act as an expert content strategist. Create text for a 5-slide Instagram carousel about: "{topic}".
        - Slide 1: A strong, scroll-stopping hook.
        - Slide 2-4: Core value and insights.
        - Slide 5: A clear Call to Action (CTA) (e.g., save, share, follow).
        Keep the text punchy and optimized for visual design on platforms like Canva.
        """
    else:
        prompt = f"Act as a professional copywriter. Write a highly engaging social media post about: {topic}"

    # يمكنك دائماً تعديل الـ prompt هنا أو إضافة حدود معينة لعدد الحروف إذا تطلب الأمر
    response = model.generate_content(prompt)
    return response.text
  
