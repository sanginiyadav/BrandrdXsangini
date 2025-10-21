from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
        ####
        
SHAYRI = [
    "🌹**तुम मेरी जिंदगी की रोशनी हो।**\n**तेरी मुस्कान मेरे दिल को खुश करती है।**\n**तुम्हारे बिना सब अधूरा लगता है।**\n**तुम मेरी हर खुशी की वजह हो।**\n\n🌹**You are the light of my life.**\n**Your smile makes my heart happy.**\n**Without you, everything feels incomplete.**\n**You are the reason for all my happiness.**",

    "🌸**तेरी यादें मुझे हर पल याद आती हैं।**\n**तेरी बातें मेरे दिल को सुकून देती हैं।**\n**तुम मेरी तन्हाई का सहारा हो।**\n**तुम मेरी खुशियों की वजह हो।**\n\n🌸**I remember you every moment.**\n**Your words give peace to my heart.**\n**You are the support of my loneliness.**\n**You are the reason for my happiness.**",

    "🌺**तुम मेरी सबसे बड़ी खुशी हो।**\n**तेरे बिना मेरी दुनिया अधूरी है।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**तुम मेरे दिल की रौशनी हो।**\n\n🌺**You are my greatest joy.**\n**Without you, my world is incomplete.**\n**Your love is priceless to me.**\n**You are the light of my heart.**",

    "🌹**तुम मेरे ख्वाबों की रानी हो।**\n**तेरे ख्यालों में हर पल खो जाता हूँ।**\n**तेरी मुस्कान मेरी दुनिया सजाती है।**\n**तुम मेरी खुशियों का कारण हो।**\n\n🌹**You are the queen of my dreams.**\n**I lose myself in thoughts of you every moment.**\n**Your smile decorates my world.**\n**You are the reason for my happiness.**",

    "🌸**तुम मेरी सुबह की सबसे प्यारी शुरुआत हो।**\n**तेरे बिना रातें अधूरी हैं।**\n**तुम मेरी हर खुशी में शामिल हो।**\n**तेरी यादें मुझे हमेशा हँसाती हैं।**\n\n🌸**You are the sweetest start of my morning.**\n**Without you, the nights are incomplete.**\n**You are part of all my happiness.**\n**Your memories always make me smile.**",

    "🌺**तुम मेरी जिंदगी का सबसे हसीन हिस्सा हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**तेरे बिना सब कुछ अधूरा लगता है।**\n**तुम मेरी खुशियों की वजह हो।**\n\n🌺**You are the most beautiful part of my life.**\n**Your love is priceless to me.**\n**Without you, everything feels incomplete.**\n**You are the reason for my happiness.**",

    "🌹**तेरी आँखों में मैं अपना आसमान देखता हूँ।**\n**तेरी मुस्कान मेरे लिए सबसे बड़ी खुशी है।**\n**तुम मेरी जिंदगी की सबसे खूबसूरत याद हो।**\n**तुम मेरी तन्हाई का सहारा हो।**\n\n🌹**I see my sky in your eyes.**\n**Your smile is my greatest joy.**\n**You are the most beautiful memory of my life.**\n**You are the support of my loneliness.**",

    "🌸**तुम मेरी धड़कनों में बसते हो।**\n**तेरे बिना मेरी दुनिया अधूरी है।**\n**तेरी हर बात मुझे खुश कर देती है।**\n**तुम मेरी हर खुशी की वजह हो।**\n\n🌸**You live in my heartbeat.**\n**Without you, my world is incomplete.**\n**Everything you say makes me happy.**\n**You are the reason for all my happiness.**",

    "🌺**तुम मेरी तन्हाई का सहारा हो।**\n**तेरे ख्यालों में मैं हर पल खो जाता हूँ।**\n**तुम मेरी खुशियों का कारण हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n\n🌺**You are the support of my loneliness.**\n**I lose myself in thoughts of you every moment.**\n**You are the reason for my happiness.**\n**Your love is priceless to me.**",

    "🌹**तुम मेरी जिंदगी की सबसे हसीन कहानी हो।**\n**तेरी यादें मुझे हर पल खुश रखती हैं।**\n**तुम मेरी सबसे बड़ी खुशी हो।**\n**तेरी मुस्कान मेरे दिल को रोशन करती है।**\n\n🌹**You are the most beautiful story of my life.**\n**Your memories make me happy every moment.**\n**You are my greatest happiness.**\n**Your smile lights up my heart.**",
   
    "🌹**तुम मेरी जिंदगी की रोशनी हो।**\n**तेरी मुस्कान मेरे दिल को खुश करती है।**\n**तुम्हारे बिना सब अधूरा लगता है।**\n**तुम मेरी हर खुशी की वजह हो।**\n\n🌹**You are the light of my life.**\n**Your smile makes my heart happy.**\n**Without you, everything feels incomplete.**\n**You are the reason for all my happiness.**",
    
    "🌸**तेरी यादें मुझे हर पल याद आती हैं।**\n**तेरी बातें मेरे दिल को सुकून देती हैं।**\n**तुम मेरी तन्हाई का सहारा हो।**\n**तुम मेरी खुशियों की वजह हो।**\n\n🌸**I remember you every moment.**\n**Your words give peace to my heart.**\n**You are the support of my loneliness.**\n**You are the reason for my happiness.**",
    
    "🌺**तुम मेरी सबसे बड़ी खुशी हो।**\n**तेरे बिना मेरी दुनिया अधूरी है।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**तुम मेरे दिल की रौशनी हो।**\n\n🌺**You are my greatest joy.**\n**Without you, my world is incomplete.**\n**Your love is priceless to me.**\n**You are the light of my heart.**",
    
    "🌹**तुम मेरे ख्वाबों की रानी हो।**\n**तेरे ख्यालों में हर पल खो जाता हूँ।**\n**तेरी मुस्कान मेरी दुनिया सजाती है।**\n**तुम मेरी खुशियों का कारण हो।**\n\n🌹**You are the queen of my dreams.**\n**I lose myself in thoughts of you every moment.**\n**Your smile decorates my world.**\n**You are the reason for my happiness.**",
    
    "🌸**तुम मेरी सुबह की सबसे प्यारी शुरुआत हो।**\n**तेरे बिना रातें अधूरी हैं।**\n**तुम मेरी हर खुशी में शामिल हो।**\n**तेरी यादें मुझे हमेशा हँसाती हैं।**\n\n🌸**You are the sweetest start of my morning.**\n**Without you, the nights are incomplete.**\n**You are part of all my happiness.**\n**Your memories always make me smile.**",
    
    "🌺**तुम मेरी जिंदगी का सबसे हसीन हिस्सा हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**तेरे बिना सब कुछ अधूरा लगता है।**\n**तुम मेरी खुशियों की वजह हो।**\n\n🌺**You are the most beautiful part of my life.**\n**Your love is priceless to me.**\n**Without you, everything feels incomplete.**\n**You are the reason for my happiness.**",
    
    "🌹**तेरी आँखों में मैं अपना आसमान देखता हूँ।**\n**तेरी मुस्कान मेरे लिए सबसे बड़ी खुशी है।**\n**तुम मेरी जिंदगी की सबसे खूबसूरत याद हो।**\n**तुम मेरी तन्हाई का सहारा हो।**\n\n🌹**I see my sky in your eyes.**\n**Your smile is my greatest joy.**\n**You are the most beautiful memory of my life.**\n**You are the support of my loneliness.**",
    
    "🌸**तुम मेरी धड़कनों में बसते हो।**\n**तेरे बिना मेरी दुनिया अधूरी है।**\n**तेरी हर बात मुझे खुश कर देती है।**\n**तुम मेरी हर खुशी की वजह हो।**\n\n🌸**You live in my heartbeat.**\n**Without you, my world is incomplete.**\n**Everything you say makes me happy.**\n**You are the reason for all my happiness.**",
    
    "🌺**तुम मेरी तन्हाई का सहारा हो।**\n**तेरे ख्यालों में मैं हर पल खो जाता हूँ।**\n**तुम मेरी खुशियों का कारण हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n\n🌺**You are the support of my loneliness.**\n**I lose myself in thoughts of you every moment.**\n**You are the reason for my happiness.**\n**Your love is priceless to me.**",
    
    "🌹**तुम मेरी जिंदगी की सबसे हसीन कहानी हो।**\n**तेरी यादें मुझे हर पल खुश रखती हैं।**\n**तुम मेरी सबसे बड़ी खुशी हो।**\n**तेरी मुस्कान मेरे दिल को रोशन करती है।**\n\n🌹**You are the most beautiful story of my life.**\n**Your memories make me happy every moment.**\n**You are my greatest happiness.**\n**Your smile lights up my heart.**",

    "💖**तुम मेरी जिंदगी का सबसे हसीन हिस्सा हो।**\n**तेरे बिना मेरी दुनिया अधूरी है।**\n**तुम्हारे बिना मैं अधूरा हूँ।**\n**क्या तुम हमेशा मेरे साथ रहोगी?**\n\n💖**You are the most beautiful part of my life.**\n**Without you, my world is incomplete.**\n**Without you, I am incomplete.**\n**Will you stay with me forever?**",

    "💘**तुम्हारी मुस्कान मेरे दिल को खुश करती है।**\n**तेरी आँखों में मैं अपना आसमान देखता हूँ।**\n**मेरे दिल की हर धड़कन तुम्हारे नाम है।**\n**क्या तुम मेरी हो जाओगी?**\n\n💘**Your smile makes my heart happy.**\n**I see my sky in your eyes.**\n**Every heartbeat of mine is in your name.**\n**Will you be mine?**",

    "💞**मैं तुम्हारे बिना कुछ भी नहीं हूँ।**\n**तुम मेरी हर खुशी की वजह हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**क्या तुम मेरी जिंदगी बनोगी?**\n\n💞**I am nothing without you.**\n**You are the reason for all my happiness.**\n**Your love is priceless to me.**\n**Will you be my life?**",

    "💖**तुम मेरे ख्वाबों की रानी हो।**\n**तेरे ख्यालों में मैं हर पल खो जाता हूँ।**\n**तेरी मुस्कान मेरी दुनिया सजाती है।**\n**क्या तुम मेरे साथ हमेशा रहोगी?**\n\n💖**You are the queen of my dreams.**\n**I lose myself in thoughts of you every moment.**\n**Your smile decorates my world.**\n**Will you stay with me forever?**",

    "💘**मेरे दिल की हर धड़कन तुम्हारे लिए है।**\n**तुम मेरी तन्हाई का सहारा हो।**\n**मेरे ख्वाब सिर्फ तुम्हारे हैं।**\n**क्या तुम मुझे अपना प्यार दोगी?**\n\n💘**Every heartbeat of mine is for you.**\n**You are the support of my loneliness.**\n**My dreams are only of you.**\n**Will you give me your love?**",

    "💞**तुम मेरी जिंदगी की सबसे हसीन कहानी हो।**\n**तेरी यादें मुझे हर पल खुश रखती हैं।**\n**तुम मेरी सबसे बड़ी खुशी हो।**\n**क्या तुम हमेशा मेरी बनोगी?**\n\n💞**You are the most beautiful story of my life.**\n**Your memories make me happy every moment.**\n**You are my greatest happiness.**\n**Will you be mine forever?**",

    "💖**तुम मेरी तन्हाई का सहारा हो।**\n**तेरे ख्यालों में मैं हर पल खो जाता हूँ।**\n**तुम मेरी खुशियों का कारण हो।**\n**क्या तुम मेरी जिंदगी बनोगी?**\n\n💖**You are the support of my loneliness.**\n**I lose myself in thoughts of you every moment.**\n**You are the reason for my happiness.**\n**Will you be my life?**",

    "💘**मेरे ख्वाबों में सिर्फ तुम हो।**\n**तुम मेरी जिंदगी का सबसे हसीन हिस्सा हो।**\n**तेरी मोहब्बत मेरे लिए अनमोल है।**\n**क्या तुम मेरे दिल को स्वीकार करोगी?**\n\n💘**Only you are in my dreams.**\n**You are the most beautiful part of my life.**\n**Your love is priceless to me.**\n**Will you accept my heart?**",

    "💞**मैं हर पल तुम्हें याद करता हूँ।**\n**तुम मेरी खुशियों का कारण हो।**\n**तेरी मुस्कान मेरे दिल को रोशन करती है।**\n**क्या तुम मेरे साथ हमेशा रहोगी?**\n\n💞**I remember you every moment.**\n**You are the reason for my happiness.**\n**Your smile lights up my heart.**\n**Will you stay with me forever?**",

    "💖**तुम मेरी जिंदगी की सबसे हसीन याद हो।**\n**तेरे बिना सब कुछ अधूरा लगता है।**\n**मेरे ख्वाब सिर्फ तुम्हारे हैं।**\n**क्या तुम मेरी हो जाओगी?**\n\n💖**You are the most beautiful memory of my life.**\n**Without you, everything feels incomplete.**\n**My dreams are only of you.**\n**Will you be mine?**",
    
    "💔**तुम्हारे जाने के बाद मेरी दुनिया सूनी हो गई।**\n**तेरी यादें अब सिर्फ दर्द देती हैं।**\n**मैंने हर खुशी खो दी।**\n**अब मैं अकेले हूँ।**\n\n💔**After you left, my world became empty.**\n**Your memories only give pain now.**\n**I have lost all happiness.**\n**Now I am alone.**",

    "💔**हम साथ नहीं हैं लेकिन यादें अभी भी हैं।**\n**दिल हर पल तुझे याद करता है।**\n**तुम्हारे बिना सब अधूरा लगता है।**\n**काश तुम लौट आओ।**\n\n💔**We are not together but memories still remain.**\n**My heart remembers you every moment.**\n**Everything feels incomplete without you.**\n**I wish you would come back.**",

    "💔**तुमसे दूर होकर मैंने खुद को खो दिया।**\n**हर खुशी अब अधूरी लगती है।**\n**दिल तन्हा और दिल टूट चुका है।**\n**तेरी यादें मुझे सताती हैं।**\n\n💔**By being away from you, I lost myself.**\n**Every happiness now feels incomplete.**\n**Heart is lonely and broken.**\n**Your memories haunt me.**",

    "💔**हमारे प्यार की कहानी खत्म हो गई।**\n**अब सिर्फ यादें बची हैं।**\n**दिल हर पल तड़पता है।**\n**काश समय को पलटा जा सके।**\n\n💔**Our love story has ended.**\n**Now only memories remain.**\n**Heart aches every moment.**\n**I wish we could turn back time.**",

    "💔**तुम्हारे बिना मेरी दुनिया सूनी है।**\n**हर खुशी अधूरी लगती है।**\n**तेरी यादें मुझे रोने पर मजबूर करती हैं।**\n**काश तुम वापस आ जाओ।**\n\n💔**Without you, my world is empty.**\n**Every happiness feels incomplete.**\n**Your memories make me cry.**\n**I wish you would return.**",

    "💔**हमारी मोहब्बत अब सिर्फ ख्वाब बन गई।**\n**तेरी यादें अब दर्द देती हैं।**\n**दिल तन्हा और टूट चुका है।**\n**मैंने सब कुछ खो दिया।**\n\n💔**Our love has now become just a dream.**\n**Your memories now give pain.**\n**Heart is lonely and broken.**\n**I have lost everything.**",

    "💔**तुम दूर चले गए और दिल टूट गया।**\n**हर खुशी अब अधूरी लगती है।**\n**तेरी यादें अब मुझे सताती हैं।**\n**काश तुम वापस आ जाओ।**\n\n💔**You went away and my heart broke.**\n**Every happiness now feels incomplete.**\n**Your memories haunt me now.**\n**I wish you would return.**",

    "💔**हमारा प्यार अब सिर्फ एक याद है।**\n**तेरी मुस्कान अब मेरे सामने नहीं है।**\n**दिल हर पल तड़पता है।**\n**मैं तन्हा रह गया हूँ।**\n\n💔**Our love is now just a memory.**\n**Your smile is no longer in front of me.**\n**Heart aches every moment.**\n**I am left lonely.**",

    "💔**तुम्हारे जाने के बाद सब बदल गया।**\n**दिल तन्हा और दुखी है।**\n**तेरी यादें अब दर्द देती हैं।**\n**काश तुम वापस आ जाओ।**\n\n💔**After you left, everything changed.**\n**Heart is lonely and sad.**\n**Your memories now give pain.**\n**I wish you would come back.**",

    "💔**हम साथ नहीं हैं लेकिन यादें अभी भी हैं।**\n**हर खुशी अधूरी लगती है।**\n**दिल तन्हा और टूट चुका है।**\n**काश तुम लौट आओ।**\n\n💔**We are not together but memories still remain.**\n**Every happiness feels incomplete.**\n**Heart is lonely and broken.**\n**I wish you would return.**",
    
    "🌌**तन्हाई में बस तुम्हारा नाम लिया है।**\n**हर ख्वाब में तुम्हारी याद आई है।**\n**दिल की धड़कन तुम्हारे लिए है।**\n**क्या तुम मेरी दुनिया बनोगी?**\n\n🌌**In loneliness, I only took your name.**\n**In every dream, I remembered you.**\n**My heartbeat is for you.**\n**Will you become my world?**",

    "💫**तेरी मुस्कान मेरे अंधेरों को रोशन कर देती है।**\n**तुम्हारे बिना सब कुछ सूना है।**\n**तेरी यादें हर पल सताती हैं।**\n**क्या तुम मेरी जिंदगी बनोगी?**\n\n💫**Your smile lights up my darkness.**\n**Without you, everything is empty.**\n**Your memories haunt me every moment.**\n**Will you be my life?**",

    "🌙**रातों में सिर्फ तुम्हारा ख्याल आता है।**\n**दिल की तन्हाई को सिर्फ तुम मिटा सकते हो।**\n**तेरे बिना नींद नहीं आती।**\n**क्या तुम मेरे पास रहोगी?**\n\n🌙**In nights, only your thought comes.**\n**You are the only one who can erase the loneliness of my heart.**\n**Without you, I can't sleep.**\n**Will you stay with me?**",

    "🔥**मेरे ख्वाब सिर्फ तुम्हारे हैं।**\n**तेरी यादें मेरे दिल को छू जाती हैं।**\n**तुम मेरी तन्हाई की वजह हो।**\n**क्या तुम हमेशा मेरे साथ रहोगी?**\n\n🔥**My dreams are only of you.**\n**Your memories touch my heart.**\n**You are the reason for my loneliness.**\n**Will you stay with me forever?**",

    "🌟**तुम्हारे बिना मेरी दुनिया अधूरी है।**\n**हर खुशी अब फीकी लगती है।**\n**दिल की हर धड़कन तुम्हारे नाम है।**\n**क्या तुम मेरी बनोगी?**\n\n🌟**Without you, my world is incomplete.**\n**Every happiness feels dull now.**\n**Every heartbeat of mine is in your name.**\n**Will you be mine?**",

    "🌌**हमारा प्यार अब सिर्फ यादें बन गया है।**\n**तेरी मुस्कान अब मेरे सामने नहीं है।**\n**दिल हर पल तड़पता है।**\n**काश तुम लौट आओ।**\n\n🌌**Our love has now become only memories.**\n**Your smile is no longer in front of me.**\n**My heart aches every moment.**\n**I wish you would return.**",

    "💫**तुम मेरी जिंदगी की सबसे खूबसूरत कहानी हो।**\n**तेरी यादें हर पल मेरे साथ हैं।**\n**तेरा नाम मेरे दिल में हमेशा रहेगा।**\n**क्या तुम मेरी दुनिया बनोगी?**\n\n💫**You are the most beautiful story of my life.**\n**Your memories are with me every moment.**\n**Your name will always remain in my heart.**\n**Will you be my world?**",

    "🌙**तुम मेरी तन्हाई की सबसे हसीन वजह हो।**\n**तेरे बिना सब कुछ अधूरा है।**\n**हर ख्वाब में तुम्हें ढूंढता हूँ।**\n**क्या तुम मेरे पास रहोगी?**\n\n🌙**You are the most beautiful reason for my loneliness.**\n**Without you, everything is incomplete.**\n**I search for you in every dream.**\n**Will you stay with me?**",

    "🔥**तेरी यादें मेरे दिल को जलाती हैं।**\n**तुम बिन मेरी दुनिया सूनी है।**\n**हर खुशी अब अधूरी लगती है।**\n**क्या तुम मेरे साथ रहोगी?**\n\n🔥**Your memories burn my heart.**\n**Without you, my world is empty.**\n**Every happiness feels incomplete now.**\n**Will you stay with me?**",

    "🌟**हमारा प्यार अब सिर्फ ख्वाब बन गया है।**\n**तेरी यादें अब दर्द देती हैं।**\n**दिल तन्हा और टूट चुका है।**\n**काश तुम वापस आओ।**\n\n🌟**Our love has now become just a dream.**\n**Your memories now give pain.**\n**Heart is lonely and broken.**\n**I wish you would return.**",

    # --------- इसी पैटर्न से 90 और शायरी add करें ---------
]
# Command
    


@app.on_message(filters.command(["shayari" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/shayaril  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["cancelshayari", "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("👣 𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐒𝐇𝐀𝐘𝐀𝐑𝐈 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 💗")
