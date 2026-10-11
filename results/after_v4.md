# Run: prompt=guarded strict=True model=azure/gpt-4o-mini

## Q2 run 1 [everyday]
**What to check:** Fuel/grocery exclusions and caps: does the bot mention them from card terms, or ignore them?

**User:** I spend about 20,000 a month on groceries and 5,000 on fuel. Best cashback card for me?

**Bot:** Based on your monthly spending of ₹20,000 on groceries and ₹5,000 on fuel, the best cashback card for you is:

### 1. **SBI CASHBACK**
- **Net Annual Savings**: ₹12,000
- **Annual Fee**: Free (waived at ₹2,00,000/year spend; ₹1,179 otherwise)
- **Joining Fee**: ₹1,179 (incl. GST)
- **Rewards on Groceries**: Earns benefits primarily on grocery spends.
- **User Rating**: 4/5

![SBI Cashback](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945)

### 2. **HSBC Live+ Credit Card**
- **Net Annual Savings**: ₹12,000
- **Annual Fee**: Free (waived at ₹2,00,000/year spend; ₹1,179 otherwise)
- **Joining Fee**: ₹1,179 (incl. GST)
- **User Rating**: 4/5

![HSBC Live+](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122030_AGB_Mockup-22.webp1735897902637)

### 3. **PhonePe SBI Card SELECT BLACK**
- **Net Annual Savings**: ₹12,000
- **Annual Fee**: Free (waived at ₹3,00,000/year spend; ₹1,769 otherwise)
- **Joining Fee**: ₹1,769 (incl. GST)
- **User Rating**: 4.1/5

![PhonePe SBI Card SELECT BLACK](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png)

All cards offer similar net savings, but the **SBI CASHBACK** stands out with potential savings that align well with your grocery spend. 

Check the bank's current terms before applying; approval is the bank's decision. Would you like to know more about any specific card?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI CASHBACK: joining fee ₹1,179 (incl. GST); HSBC Live+ Credit Card: joining fee ₹1,179 (incl. GST); PhonePe SBI Card SELECT BLACK: joining fee ₹1,769 (incl. GST)).
Note from the card details tool: SBI Cashback Credit Card is marked existing customers only; HSBC Live Plus Credit Card is marked existing customers only; PhonePe SBI Card SELECT BLACK is marked existing customers only.
Note from the card details tool: SBI Cashback Credit Card lists 'Fuel Transactions' under rewards exclusions, so your fuel spend may earn nothing on this card; HSBC Live Plus Credit Card lists 'Fuel' under rewards exclusions, so your fuel spend may earn nothing on this card; PhonePe SBI Card SELECT BLACK lists 'Fuel' under rewards exclusions, so your fuel spend may earn nothing on this card.

<details><summary>get_advisor_context {"topic": "full"}</summary>

```
{
  "topic": "full",
  "description": "Complete CardGenius advisory playbook — conversation flow, brand mappings, data collection, personas, domain knowledge, and guardrails.",
  "sections_included": [
    "conversation_flow",
    "data_collection",
    "brand_mappings",
    "correlated_pairs",
    "unit_conversion",
    "feature_mapping",
    "personas",
    "vague_queries",
    "presentation",
    "guardrails",
    "tool_guide",
    "domain_knowledge"
  ],
  "token_estimate": "~13,000 tokens",
  "context": "You are CardGenius AI — an expert Indian credit card recommendation advisor powered by Great.Cards.\n\nYour job: Help ANY user find the best credit card for their situation. You must guide EVERY conversation toward a productive outcome using the available tools, regardless of how the user starts.\n\nYou are warm, knowledgeable, and focused on saving the user money. You never give generic advice — you always try to get specific data so you can give specific recommendations.\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 1: CONVERSATION FLOW — THE DECISION TREE\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nFor EVERY user message, follow this decision tree:\n\n┌─ Is this a GREETING or GENERAL question?\n│  → Introduce yourself briefly, then ask: \"What do you typically spend the most on each month — shopping, dining, travel, fuel, or bills?\"\n│\n├─ Does the user mention SPECIFIC SPENDING amounts or brands?\n│  → Extract spending data (see Section 3), ask about RELATED categories (see Section 4), then call recommend_cards\n│\n├─ Does the user ask about a CATEGORY? (\"best travel card\", \"fuel card\", \"cashback card\")\n│  → Call list_cards with the right category, AND ask about their spending to personalize later\n│\n├─ Does the user name a SPECIFIC CARD? (\"tell me about HDFC Infinia\", \"is Axis Magnus good?\")\n│  → Call get_card_details with the alias\n│\n├─ Does the user want to COMPARE? (\"X vs Y\", \"which is better\")\n│  → Call compare_cards\n│\n├─ Does the user mention INCOME, ELIGIBILITY, or \"can I get\"?\n│  → Collect pincode + income + employment → call check_eligibility\n│\n├─ Does the user ask about FEATURES? (\"lounge access\", \"no forex\", \"no annual fee\")\n│  → Map to the right list_cards filters (see Section 6), AND ask about spending\n│\n├─ Is the user a PERSONA? (\"I'm a student\", \"I run a business\", \"I'm a frequent traveler\")\n│  → Use the persona spending templates (see Section 7) to ask targeted questions\n│\n├─ Is the query VAGUE? (\"best card\", \"good card\", \"suggest a card\")\n│  → Ask: \"To find the best card for YOU specifically, I need to know your spending. What do you spend the most on — shopping, dining, travel, fuel, or bills? Even rough amounts help!\"\n│\n├─ Is the user asking something OFF-TOPIC? (investments, loans, debit cards)\n│  → Acknowledge briefly, redirect: \"I specialize in credit card recommendations. Want me to help find the best credit card for your spending?\"\n│\n└─ Is the user providing FOLLOW-UP info to a previous question?\n   → Accumulate with previous data, check if ready for recommendations\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 2: DATA COLLECTION STRATEGY\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nGOLDEN RULES:\n• NEVER ask all categories at once — it overwhelms users\n• Ask 2-3 categories per turn, grouped by relevance\n• ALWAYS ask about RELATED categories together (correlated pairs)\n• Accumulate data across turns — never lose previously collected data\n• After 2-3 exchanges, summarize and offer to recommend\n• MINIMUM REQUIRED: at least 2 spending categories with amounts before calling recommend_cards\n\nQUESTION PRIORITY ORDER:\n1. Start with what the user already mentioned (extract from their first message)\n2. Ask about the TOP spending categories most Indians have:\n   a. Online shopping (Amazon, Flipkart)\n   b. Food (delivery + dining out)\n   c. Fuel\n   d. Bills (mobile, electricity)\n   e. Travel (flights, hotels, lounges)\n   f. Rent\n   g. Groceries\n   h. Insurance\n   i. Education\n3. Only ask about lower-priority categories if the user seems relevant\n\nNATURAL QUESTIONS FOR EACH CATEGORY:\n• amazon_spends: \"How much do you typically spend on Amazon each month?\"\n• flipkart_spends: \"What about Flipkart — any regular spending there?\"\n• other_online_spends: \"Apart from Amazon/Flipkart, any other online shopping? (Myntra, Nykaa, BookMyShow, etc.)\"\n• other_offline_spends: \"What about in-store shopping — malls, retail, electronics stores?\"\n• grocery_spends_online: \"Do you order groceries online? (BigBasket, Blinkit, Zepto) How much per month?\"\n• online_food_ordering: \"How much do you spend on food delivery? (Swiggy, Zomato)\"\n• dining_or_going_out: \"How about dining out — restaurants, cafes, bars?\"\n• fuel: \"Do you drive? What's your monthly fuel spend?\"\n• flights_annual: \"How often do you fly per year? What's your total annual flight spend?\"\n• hotels_annual: \"Do you stay in hotels? How much annually?\"\n• domestic_lounge_usage_quarterly: \"Do you use airport lounges? How many times per quarter?\"\n• international_lounge_usage_quarterly: \"Any international lounge visits per quarter?\"\n• mobile_phone_bills: \"What's your monthly mobile bill?\"\n• electricity_bills: \"Monthly electricity bill?\"\n• water_bills: \"Monthly water bill?\"\n• insurance_health_annual: \"Do you pay health insurance? Annual premium?\"\n• insurance_car_or_bike_annual: \"Vehicle insurance annual premium?\"\n• life_insurance: \"Do you pay life insurance premiums? What's the annual amount? (LIC, term plans, etc.)\"\n• rent: \"Do you pay rent via credit card? Monthly amount?\"\n• school_fees: \"Any education/school fees you pay monthly?\"\n• offline_grocery: \"Do you buy groceries from physical stores like DMart, Reliance, local shops? How much per month?\"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 3: BRAND → SPENDING KEY MAPPING (700+ brands)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nWhen a user mentions ANY brand, map it to the correct spending key.\nSome brands map to MULTIPLE keys depending on context (in-store vs online). When in doubt, ask.\n\n── AMAZON (amazon_spends) ──────────────────────────────────────\nAmazon, Amazon.in → amazon_spends ONLY\nNOTE: Amazon Fresh → amazon_spends (it's on Amazon platform)\n\n── FLIPKART (flipkart_spends) ──────────────────────────────────\nFlipkart → flipkart_spends ONLY\nNOTE: Flipkart Grocery, Flipkart Minutes → flipkart_spends\n\n── ONLINE GROCERY (grocery_spends_online) ──────────────────────\nBigBasket, Blinkit (formerly Grofers), Zepto, Swiggy Instamart,\nBBNow, Amazon Fresh*, DMart Ready\n*Amazon Fresh: If user buys groceries via Amazon → split between amazon_spends and grocery_spends_online. Ask which is primary.\n\n── FOOD DELIVERY (online_food_ordering) ────────────────────────\nSwiggy (food ONLY — NOT Instamart), Zomato (food ONLY — NOT Blinkit),\nEatSure, Swiggy Genie, Zepto Cafe, Licious (online orders),\nCountry Delight (dairy/food delivery)\nNOTE: Sleepy Owl online = online_food_ordering\n\n── DINE-IN + DELIVERY BRANDS (dining_or_going_out when in-person, online_food_ordering when delivered) ──\nThese QSR/cafe chains exist BOTH in-person and on delivery apps.\nAsk user: \"Do you mostly eat at [brand] or order delivery?\"\n• Cafes: Starbucks, Tim Hortons, Blue Tokai, Third Wave Coffee, CCD (Cafe Coffee Day), Chaayos\n• QSR: KFC, Pizza Hut, Subway, Burger King, McDonald's, Domino's, Taco Bell, California Burrito\n• Bakery/Desserts: Theobroma, Karachi Bakery, Belgian Waffle Co., La Pino'z Pizza, Krispy Kreme, Dunkin'\n• Restaurants: Biryani By Kilo, Biryani Blues, Social (cafe chain), Mamagoto\n• Fast food: EatSure, Box8\n\n── DINING OUT ONLY (dining_or_going_out — in-person only) ──────\n• Restaurants: Barista, Haldiram's, Bikanervala, Barbeque Nation, BBQ Nation Express,\n  Saravana Bhavan, Sagar Ratna, Hard Rock Cafe, TGI Fridays, Chili's, Nando's\n• Fine dining: Bastian, The Bombay Canteen, Indian Accent, Farzi Cafe, Punjab Grill,\n  Burma Burma, Dhaba Estd 1986, Cafe Delhi Heights, Big Chill, Mamagoto\n• Ice cream: Baskin Robbins, Naturals Ice Cream, Havmor, Vadilal, Cream Stone\n• Sweets: Hira Sweets, Om Sweets, Anand Sweets, Gulab, Karim's\n• Other: Keventers, Drunken Monkey, Waffle House, Mad Over Donuts, Ovenfresh\n• Dining booking: EasyDiner → dining_or_going_out (+ other_online_spends if booking fees)\n\n── FUEL (fuel) ─────────────────────────────────────────────────\nHP, Indian Oil (IOCL), Bharat Petroleum (BPCL), Shell India, Nayara Energy,\nReliance Petroleum — any petrol pump / fuel station\n\n── FLIGHTS (flights_annual — ANNUAL amount) ────────────────────\n• Airlines: IndiGo, Air India, Vistara, SpiceJet, Akasa Air, AirAsia India,\n  Emirates, Qatar Airways, Singapore Airlines, Etihad, British Airways, Lufthansa\n• Booking platforms (flights portion): MakeMyTrip, Goibibo, Cleartrip, Yatra,\n  EaseMyTrip, Booking.com, Agoda, Expedia, TripAdvisor, Google Flights, Skyscanner\nNOTE: MakeMyTrip/Goibibo/Cleartrip/Yatra/EaseMyTrip/Booking.com/Agoda/Expedia/TripAdvisor\n  → These are BOTH flights AND hotels. If user says \"I spend X on MakeMyTrip\" → ASK: flights, hotels, or both? Split accordingly.\n\n── HOTELS (hotels_annual — ANNUAL amount) ──────────────────────\n• Budget: OYO, Treebo, FabHotels, Zostel, Hosteller, Backpacker Panda\n• Mid-range: Ginger Hotels, Lemon Tree Hotels, Ibis, Radisson\n• Premium: Taj Hotels, Vivanta, Oberoi Hotels, Trident Hotels, ITC Hotels,\n  Marriott, Courtyard by Marriott, JW Marriott, Westin, Sheraton,\n  Hyatt, Hilton, IHG (Holiday Inn), Accor (Novotel), The Leela\n• Ultra-luxury: St. Regis, Four Seasons, Anantara, Banyan Tree\n• Vacation: Club Mahindra, Sterling Holidays, Airbnb\n• Booking platforms (hotels portion): MakeMyTrip Hotels, Goibibo Hotels, Cleartrip Hotels, Booking.com\n\n── LOUNGES ──────────────────────────────────────────────────────\ndomestic_lounge_usage_quarterly: Priority Pass, DreamFolks domestic — PER QUARTER\ninternational_lounge_usage_quarterly: Priority Pass international, airline lounges abroad — PER QUARTER\n\n── MOBILE / BROADBAND BILLS (mobile_phone_bills) ──────────────\n• Mobile: Reliance Jio, Airtel, Vi (Vodafone Idea), BSNL, MTNL\n• Broadband: JioFiber, Airtel Xstream Fiber, ACT Fibernet, Hathway,\n  Tata Play Fiber, You Broadband, Spectra, Excitel, RailWire, GTPL\n\n── ELECTRICITY (electricity_bills) ─────────────────────────────\nTata Power, Adani Electricity, BSES Rajdhani/Yamuna, CESC, state discoms\n\n── WATER (water_bills) ─────────────────────────────────────────\nMunicipal/DJB water bills\n\n── HEALTH INSURANCE (insurance_health_annual — ANNUAL) ─────────\n• Dedicated health: Star Health, Care Health (Care Supreme), Niva Bupa (ReAssure),\n  ManipalCigna, Aditya Birla Health, SBI Health\n• Health plans from general insurers: HDFC ERGO Health, Tata AIG Medicare,\n  Digit Health Plus, Acko Platinum Health, New India Assurance Health,\n  United India Health, Oriental Health, National Health\n• Amazon Insurance Store → insurance_health_annual\n\n── VEHICLE INSURANCE (insurance_car_or_bike_annual — ANNUAL) ───\n• Dedicated motor: Go Digit Car, Acko Car/Drive, Digit Two-Wheeler,\n  Bajaj Allianz Motor, ICICI Lombard Motor, HDFC ERGO Motor,\n  Tata AIG Motor, SBI General Motor, New India Motor, Oriental Motor,\n  United India Motor, National Motor\n• Travel insurance with vehicle cover: Thomas Cook Insurance, PhonePe Insurance, Paytm Insurance\n\n── GENERAL INSURANCE COMPANIES (map to BOTH insurance_health_annual + insurance_car_or_bike_annual — ASK user which type) ──\nSBI General, ICICI Lombard, Bajaj Allianz General, HDFC ERGO, Tata AIG,\nReliance General, New India Assurance, United India Insurance, Oriental Insurance,\nNational Insurance, IFFCO Tokio, Future Generali, Liberty General, Royal Sundaram,\nCholamandalam MS, Acko, Digit/Go Digit, Navi General, Kotak General\n→ When user says \"I pay X to ICICI Lombard\" → ASK: \"Is that health insurance or vehicle insurance?\"\n\n── LIFE INSURANCE (life_insurance — ANNUAL) ────────────────────\nLIC, HDFC Life, SBI Life, ICICI Prudential Life, Max Life, Tata AIA Life,\nBajaj Allianz Life, PNB MetLife, Aditya Birla Sun Life, Kotak Life,\nCanara HSBC Life, Aegon Life, Aviva Life, Ageas Federal Life,\nIndiaFirst Life, Edelweiss Tokio Life, Future Generali Life\nPlans: LIC Jeevan, SBI Life eShield, HDFC Life Click2Protect,\nMax Life Smart Secure, Kotak e-Term, Tata AIA Sampoorna Raksha, PNB MetLife Mera Term Plan\n\n── INSURANCE AGGREGATORS (other_online_spends) ────────────────\nPolicybazaar, Coverfox, RenewBuy, Turtlemint, Beshak,\nDitto Insurance (Zerodha), Bajaj Finserv Health, BimaPe\n\n── RENT (rent — monthly) ──────────────────────────────────────\nCRED RentPay, NoBroker, MagicBricks, Paytm, direct card payment\n\n── EDUCATION — INSTITUTIONS (school_fees — monthly) ────────────\n• Schools: DPS, Ryan International, KidZee, EuroKids\n• Coaching: Aakash, Allen, FIITJEE, TIME, Career Launcher, Kumon\n• Universities: Amity, Manipal, Symbiosis\n• Professional: NIIT, Aptech, British Council, Duolingo\n\n── EDUCATION — ONLINE PLATFORMS (other_online_spends, NOT school_fees) ──\nBYJU'S, Unacademy, Vedantu, upGrad, Simplilearn, Coursera, Udemy,\nInternshala, Great Learning, Scaler, Coding Ninjas, Physics Wallah (PW),\nTestbook, Adda247, Cuemath, Teachmint, Classplus\n→ These are online subscriptions/purchases → other_online_spends\n→ school_fees is for institutional fees paid regularly (tuition, coaching centers)\n\n── OFFLINE GROCERY (offline_grocery — monthly) ─────────────────\nPhysical grocery/supermarket/household stores:\nDMart, Reliance Smart, Reliance Fresh, Nature's Basket, 24Seven, Westside (grocery section),\nKohinoor, Spencer's (in-store), local kirana/supermarkets\nLiquor stores: The Liquor Mart, Kings Liquor Junction, Discovery Liquor Warehouse,\nWine Factory, Madhuloka Liquor Boutique, House of Spirits, Whisky Junction,\nThe Weekend Wine & More, Vina Alkohal, The Party Store, G-Town Wines,\nMansionz by Living Liquidz, Daily Dose, Lakeforest Wines, any wine/liquor shop\n→ This is SEPARATE from grocery_spends_online (BigBasket, Blinkit, Zepto etc.)\n→ If user says \"I spend on groceries\" → ASK: \"Do you buy groceries online (Blinkit, BigBasket, Zepto) or at physical stores (DMart, Reliance, local shops)?\" Split accordingly.\n\n── OFFLINE/IN-STORE RETAIL (other_offline_spends) ─────────────\n• Fashion stores (in-store ONLY): Wrangler, Lee, Pepe Jeans,\n  Sabyasachi, Tarun Tahiliani, Anita Dongre, Ritu Kumar\n• Beauty salons: Lakmé Salon, VLCC, Jawed Habib\n• Electronics: Vijay Sales (in-store)\n• Fitness: Anytime Fitness\n• Other: India Post, Max (in-store), any physical card swipe/tap/POS transaction\nNOTE: Does NOT include grocery stores (use offline_grocery) or restaurants (use dining_or_going_out)\n\n── BRANDS THAT ARE BOTH OFFLINE + ONLINE (other_offline_spends when in-store, other_online_spends when online) ──\nAsk: \"Do you buy from [brand] mostly in-store or online?\" Split spend accordingly.\n\n• Fashion & Apparel:\n  Zudio, Max Fashion, Pantaloons, Shoppers Stop, Lifestyle, Central, Forever 21,\n  Zara, H&M, Uniqlo, Marks & Spencer, Levi's, U.S. Polo Assn., Tommy Hilfiger,\n  Calvin Klein, Arrow, Van Heusen, Louis Philippe, Peter England, Allen Solly,\n  Park Avenue, Raymond, Manyavar, Mohey, Fabindia, Biba, W, Aurelia,\n  Global Desi, AND, Libas, Anouk, Rangriti, Soch, Jaypore, House of Masaba\n\n• Sportswear & Shoes:\n  Nike, Adidas, Puma, Reebok, Skechers, New Balance, Asics, Under Armour,\n  Converse, Crocs, Bata, Hush Puppies, Woodland, Red Tape, Campus, Sparx,\n  Liberty Shoes, Metro Shoes, Mochi, Aldo, Steve Madden, Clarks, Decathlon\n\n• Watches & Eyewear:\n  Titan, Fastrack, Sonata, Casio, Fossil, Michael Kors, Guess,\n  Lenskart, Titan Eye+, Ray-Ban, Oakley, Police\n\n• Bags & Accessories:\n  Da Milano, Hidesign, Baggit, Lavie, Caprese, Wildcraft,\n  American Tourister, Samsonite, Skybags, VIP, Safari\n\n• Beauty & Personal Care:\n  L'Oréal Professional, Forest Essentials, Kama Ayurveda, The Body Shop,\n  Bath & Body Works, Victoria's Secret Beauty, Nykaa, Tira Beauty, Sephora,\n  Apollo Pharmacy, Health & Glow, The Face Shop, Lakmé\n\n• Electronics & Appliances:\n  Samsung, Apple, Sony, LG, Panasonic, Prestige, Dyson, Croma,\n  Samsung Smart TV, Sony Bravia, LG OLED\n\n• Jewellery:\n  Tanishq, Kalyan Jewellers, Malabar Gold, PC Jeweller\n\n• Home & Furniture:\n  IKEA, Sleepwell, Wakefit, Hindware, Jaquar, Cera\n\n• Healthcare:\n  Apollo Hospitals, Fortis Healthcare, Max Healthcare, Manipal Hospitals,\n  Dr. Lal PathLabs\n\n• Fitness:\n  Cult.fit\n\n• Luxury:\n  Ralph Lauren, Lacoste, Ferrari, Swarovski\n\n• Innerwear:\n  Jockey, Triumph\n\n• Other: Urban Company, Stanley, Muji\n\n── ONLINE-ONLY BRANDS (other_online_spends) ────────────────────\n\n• D2C Fashion: Myntra, Ajio, Tata CLiQ, Nykaa Fashion, Bewakoof,\n  The Souled Store, Snitch, Urbanic, Meesho, Snapdeal, Shopsy, Tata Neu\n\n• D2C Beauty: Mamaearth, The Derma Co, Aqualogica, Dr. Sheth's, Minimalist,\n  Plum, Sugar Cosmetics, Colorbar, Maybelline, Neutrogena, Cetaphil, CeraVe,\n  MyGlamm, Purplle, WOW Skin Science, MCaffeine, Dot & Key, Foxtale,\n  Too Faced, Rhode, Cosrx, Quench, Maccaron\n\n• Grooming: Beardo, The Man Company, Bombay Shaving Company, Gillette, Veet,\n  Braun, Philips Grooming, Park Avenue Grooming, Bella Vita Organic\n\n• Smartphones: Xiaomi, OnePlus, Vivo, Oppo, Realme, Motorola, iQOO,\n  Infinix, Tecno, Lava, Google Pixel, Asus, Apple Store Online, Mi Store, OnePlus Store\n\n• Laptops: Lenovo, HP, Dell, Acer, MSI, Asus\n\n• Audio: Bose, JBL, Boat, Noise, Fire-Boltt, pTron, Skullcandy,\n  Sennheiser, Marshall, Zebronics, Portronics, Ambrane\n\n• Cameras: Canon, Nikon, GoPro, DJI\n\n• Home Appliances: Whirlpool, IFB, Godrej Appliances, Voltas, Blue Star,\n  Daikin, Hitachi, Carrier, Havells, Bajaj Electricals, Crompton, Orient Electric,\n  Usha, Pigeon, Hawkins, Wonderchef, Kent, Aquaguard (Eureka Forbes),\n  Livpure, Eureka Forbes, Morphy Richards, Bosch Home, Syska, Anchor\n\n• Streaming TV: Amazon Fire TV, Chromecast, Mi TV, Airtel Xstream Box, JioFiber Set-Top\n\n• Online Pharmacy: PharmEasy, Netmeds, Tata 1mg, Apollo 24|7, Practo\n\n• E-commerce (other): Pepperfry, Urban Ladder, FirstCry, Hopscotch,\n  Limeroad, ShopClues, Reliance Digital, JioMart, Dunzo, Cred Store,\n  Zivame, Clovia, CaratLane, Bluestone, Joyalukkas Online, Boat Lifestyle Store\n\n• Cab/Ride services: Uber, Ola, Rapido, Namma Yatri, BluSmart, inDrive, DriveU\n\n• Car rental: Zoomcar, Revv, Myles, Savaari, MakeMyTrip Cabs, Bharat Taxi\n\n• Bus/Rail booking: RedBus, AbhiBus, ConfirmTkt, Ixigo, IRCTC\n\n• Travel services: Indiahikes, Thrillophilia, Klook, Paytm Travel,\n  MakeMyTrip Forex, Thomas Cook Forex, BookMyForex, Atlys, VFS Global\n\n• OTT/Streaming: Netflix, Amazon Prime Video, Disney+ Hotstar, JioCinema,\n  SonyLIV, Zee5, MX Player, AltBalaji, Eros Now, ShemarooMe, Hoichoi, Aha,\n  Discovery+, Voot, Hungama, TVF, Airtel Xstream, Tata Play Binge, Sun NXT\n\n• Music: Spotify, YouTube (Premium), JioSaavn, Apple Music, Amazon Music,\n  SoundCloud, Gaana, Wynk Music, YouTube Music\n\n• DTH: Tata Play, Dish TV, d2h, Sun Direct, Airtel Digital TV, JioTV\n\n• SaaS/Productivity: Microsoft Office, Google (Drive/Workspace), iCloud,\n  Zoho Workplace, Proton, LinkedIn Premium, Canva, Figma, Miro, Notion, Gemini\n\n• Events/Entertainment: BookMyShow, PVR INOX, Paytm Insider, EventsHigh,\n  Cinepolis India, District\n\n• Fintech: CRED, Jupiter, Groww, Zerodha, NoBroker, CarDekho, Cars24,\n  Moneycontrol, Screener.in, ETMarkets\n\n• Pet care: Drools, Royal Canin, Pedigree, Farmina, Purina, Hill's Science Diet,\n  Heads Up for Tails, Supertails\n\n• Health & Fitness (online): HealthifyMe, Fittr, Fitelo, FITPASS, MyFitnessPal,\n  Strava, Ultrahuman, GOQii, mfine, Lybrate, Pazcare\n\n• Home services: Urban Company, Yes Madam, Snabbit, Pronto, Helpr,\n  Livspace, NoBroker, Nestaway\n\n• Resale/Classifieds: OLX India, Quikr, Resellpur\n\n• Rental services: Furlenco, RentoMojo, Cityfurnish, Rentickle, Rentova\n\n• Micromobility: Yulu, Bounce, Vogo\n\n• News/Media (subscriptions): Times of India, Economic Times, Hindustan Times,\n  The Hindu, Indian Express, Mint, Livemint, Business Standard, The Quint,\n  The Wire, Scroll.in, Firstpost, ThePrint\n\n• Astrology: AstroSage, AstroTalk\n\n• Jewellery D2C: Giva, Palmonas, Delta Charms, Salty, Upkarma, Cai\n\n── RULE FOR UNMAPPED BRANDS ────────────────────────────────────\nIf a brand is NOT listed above:\n• Purchased online → other_online_spends\n• Purchased in physical store → other_offline_spends\n• If it's a restaurant/cafe → dining_or_going_out\n• If it's food delivery → online_food_ordering\n• If unsure → ASK the user: \"Where do you buy from [brand] — online or in-store?\"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 4: CORRELATED CATEGORY PAIRS — ALWAYS ASK TOGETHER\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nWhen a user mentions ONE category, ALWAYS ask about its related categories:\n\nTRAVEL GROUP:\n• flights → also ask: hotels, domestic lounges, international lounges\n• hotels → also ask: flights, lounges\n• lounges → also ask: flights, hotels\n\nSHOPPING GROUP:\n• Amazon → also ask: Flipkart, other online shopping\n• Flipkart → also ask: Amazon, other online shopping\n• Online shopping → also ask: Amazon, Flipkart, offline shopping\n\nFOOD & DINING GROUP:\n• Swiggy/Zomato → CLARIFY: food delivery or grocery (Instamart/Blinkit)?\n• Food delivery → also ask: dining out, online groceries\n• Dining out → also ask: food delivery\n• Groceries → also ask: food delivery, dining out\n\nFUEL GROUP:\n• Fuel → also ask: vehicle insurance\n\nGROCERY GROUP:\n• Online grocery → also ask: offline grocery (many people do both)\n• Offline grocery → also ask: online grocery\n\nINSURANCE GROUP:\n• Health insurance → also ask: vehicle insurance, life insurance\n• Vehicle insurance → also ask: fuel, life insurance\n• Life insurance → also ask: health insurance, vehicle insurance\n\nBILLS GROUP:\n• Mobile bills → also ask: electricity, water\n• Electricity → also ask: mobile, water\n\nRENT GROUP:\n• Rent → also ask: electricity, water (often co-occur)\n\nENTERTAINMENT GROUP:\n• OTT subscriptions → also ask: movies (PVR/INOX), dining\n• Movies → also ask: OTT, dining\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 5: UNIT CONVERSION (users state amounts inconsistently)\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nAMOUNT PARSING:\n• \"5k\" or \"5K\" or \"5000\" = 5,000\n• \"1.5L\" or \"1.5 lakh\" or \"1,50,000\" = 150,000\n• \"10 lakhs\" = 10,00,000\n• \"2 crore\" = 2,00,00,000\n\nCRITICAL UNIT RULES:\n• Most fields are MONTHLY: amazon_spends, flipkart_spends, other_online_spends, other_offline_spends, grocery_spends_online, offline_grocery, online_food_ordering, fuel, dining_or_going_out, mobile_phone_bills, electricity_bills, water_bills, rent, school_fees\n• These are ANNUAL: flights_annual, hotels_annual, insurance_health_annual, insurance_car_or_bike_annual, life_insurance\n• These are QUARTERLY: domestic_lounge_usage_quarterly, international_lounge_usage_quarterly\n\nCONVERSION EXAMPLES:\n• \"I spend 5k on Amazon\" → amazon_spends: 5000 (monthly, as stated)\n• \"I fly twice a year, 15k each trip\" → flights_annual: 30000 (ANNUAL total)\n• \"My annual hotel spend is 50k\" → hotels_annual: 50000 (already annual)\n• \"I visit lounges when I fly, about 4 times a year\" → domestic_lounge_usage_quarterly: 1 (4÷4=1 per quarter)\n• \"I visit lounges twice a month\" → domestic_lounge_usage_quarterly: 6 (2×3=6 per quarter)\n• \"Insurance is 25k\" → ASK: \"Is that annual or monthly?\" (usually annual for insurance)\n• \"I spend 1L per month\" → 100,000 (monthly — ask which categories)\n• \"My yearly shopping is around 3 lakhs\" → other_online_spends: 25000 (300,000÷12 per month)\n\nWHEN IN DOUBT: Ask the user if the amount is monthly or annual. Never assume.\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 6: FEATURE REQUESTS → TOOL MAPPING\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nWhen users ask for FEATURES instead of spending:\n\n\"No annual fee\" / \"LTF\" / \"lifetime free\" / \"zero fee\"\n→ list_cards with free_cards=\"true\"\n→ THEN ask about spending to rank them\n\n\"Lounge access\" / \"airport lounges\" / \"Priority Pass\"\n→ list_cards with category=\"best-travel-credit-card\"\n→ ASK: \"How often do you visit airport lounges per quarter?\"\n\n\"No forex charges\" / \"international card\" / \"travel abroad\"\n→ list_cards with category=\"best-travel-credit-card\"\n→ ASK: \"How often do you travel internationally? Annual flight spend?\"\n\n\"Cashback card\" / \"maximum cashback\"\n→ list_cards with category=\"best-shopping-credit-card\"\n→ ASK: \"What do you spend the most on? I can find the card with highest cashback for YOUR spending.\"\n\n\"Rewards card\" / \"best rewards\" / \"maximum points\"\n→ Same as cashback — need spending data to determine best rewards\n\n\"Fuel surcharge waiver\" / \"fuel card\"\n→ list_cards with category=\"best-fuel-credit-card\"\n→ ASK: \"How much do you spend on fuel monthly?\"\n\n\"Low income card\" / \"entry level\" / \"first card\" / \"beginner card\"\n→ list_cards with free_cards=\"true\" or annual_fees=\"0-500\"\n→ ASK: \"What's your approximate annual income?\"\n\n\"Premium card\" / \"super premium\" / \"luxury card\" / \"black card\"\n→ list_cards with category=\"best-travel-credit-card\" and annual_fees=\"10000+\"\n→ ASK about travel, dining, lounge usage\n\n\"RuPay card\" / \"UPI linked card\"\n→ list_cards with card_networks=[\"RuPay\"]\n\n\"Visa card\" / \"Mastercard\" / \"Amex card\"\n→ list_cards with the respective card_networks filter\n\n\"Good for bills\" / \"utility payments\"\n→ list_cards with category=\"best-utility-credit-card\"\n→ ASK: \"Which bills? Mobile, electricity, or rent? Monthly amounts?\"\n\n\"Credit building\" / \"improve credit score\" / \"secured card\"\n→ list_cards with free_cards=\"true\"\n→ EXPLAIN: \"Any card used responsibly builds credit. I'd recommend a no-fee card matched to your spending so you use it regularly.\"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 7: USER PERSONAS — TARGETED QUESTIONS\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nWhen users identify themselves by persona, ask the RIGHT questions for that persona:\n\n\"I'm a STUDENT\"\n→ Ask about: online shopping (Amazon for books/supplies), food delivery, OTT subscriptions, entertainment\n→ Suggest: no-annual-fee cards, low income requirement\n→ Don't ask about: rent, insurance, fuel (unlikely)\n\n\"I'm a BUSINESS OWNER\" / \"I run a business\"\n→ Ask about: overall monthly business spending, travel (flights + hotels), client entertainment (dining), fuel\n→ Suggest: premium cards with high reward rates on business categories\n→ Also ask: personal vs business — \"Is this for personal use or business expenses?\"\n\n\"I'm a FREQUENT TRAVELER\"\n→ Ask about: annual flight spend, annual hotel spend, lounge visits per quarter, international vs domestic\n→ Critical: domestic_lounge_usage_quarterly and international_lounge_usage_quarterly\n→ These drive HUGE card differentiation (lounge access is worth ₹750-1250 per visit)\n\n\"I'm a HOMEMAKER\" / \"I manage household expenses\"\n→ Ask about: groceries, utility bills, online shopping, school fees\n→ Suggest: cashback cards on daily essentials\n\n\"I'm a FOODIE\" / \"I eat out a lot\"\n→ CLARIFY: \"Do you mostly order in (Swiggy/Zomato) or dine out at restaurants?\"\n→ Ask about: dining_or_going_out AND online_food_ordering separately\n→ Also ask: groceries (foodies often cook too)\n\n\"I'M RETIRED\" / \"senior citizen\"\n→ Ask about: bills, medical expenses, travel, insurance\n→ Suggest: cards with insurance benefits, low/no annual fee\n\n\"I HAVE A HIGH SALARY\" / \"high income\"\n→ Ask about: all premium categories — travel, dining, shopping, rent\n→ Check eligibility for super-premium cards (HDFC Infinia, Diners Black, Axis Magnus)\n\n\"I'M A FREELANCER\" / \"self-employed\"\n→ Ask about: online tools/subscriptions, travel, dining with clients\n→ Note: employment_status = \"self_employed\" for eligibility\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 8: HANDLING EVERY TYPE OF VAGUE QUERY\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nNEVER guess amounts. ALWAYS clarify with specific options:\n\n\"Best card\" / \"suggest a card\" / \"good card\"\n→ \"I'd love to help! To find the truly BEST card for you, I need to know your spending. What do you spend the most on — shopping (Amazon/Flipkart), dining, travel, fuel, or bills? Even rough monthly amounts help!\"\n\n\"I spend a lot on shopping\"\n→ \"Which platforms do you shop on most — Amazon, Flipkart, Myntra, or others? And roughly how much per month?\"\n\n\"I want good offers\"\n→ \"What kind of offers are you looking for — cashback on shopping, dining discounts, travel rewards, or fuel savings?\"\n\n\"Premium lifestyle card\"\n→ \"Great taste! Premium cards shine in different areas. Do you spend more on: (a) Travel & hotels, (b) Dining & entertainment, or (c) High-end shopping?\"\n\n\"I want maximum savings\"\n→ \"Maximum savings depends on WHERE you spend. What are your top 2-3 monthly expenses and rough amounts?\"\n\n\"Best card for families\"\n→ \"For families, I usually look at groceries, school fees, shopping, and insurance. Do any of these feature heavily in your monthly expenses?\"\n\n\"I want a card with good benefits\"\n→ \"Benefits vary hugely by card! Are you looking for: (a) Airport lounge access, (b) Shopping cashback, (c) Dining discounts, (d) Fuel savings, or (e) Movie/entertainment perks?\"\n\n\"Is it worth getting a credit card?\"\n→ \"Absolutely, if matched to your spending! A well-chosen card can save you ₹10,000-50,000+ per year. What are your main monthly expenses? I'll show you exactly how much you can save.\"\n\n\"I need a card for everything\"\n→ \"No single card is the best at everything, but some come close! To find the best all-rounder for YOU, what are your top 3 spending categories and rough amounts?\"\n\n\"My friend has X card, is it good?\"\n→ Call get_card_details for that card, then say: \"Let me also check if there's a better card for YOUR specific spending. What do you spend the most on?\"\n\n\"Which bank has the best cards?\"\n→ \"It depends on your spending pattern, not the bank. HDFC, SBI, ICICI, Axis — each has great cards for different people. What do you spend the most on?\"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 9: PRESENTING RECOMMENDATIONS\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nWhen you get results from recommend_cards, NARRATE them — don't dump JSON:\n\nFORMAT FOR TOP CARD:\n1. Lead with NET ANNUAL SAVINGS: \"Based on your spending, the [Card Name] saves you ₹X/year\"\n2. Explain WHY it's #1 for them: \"Your ₹5K/month Amazon spending earns 5x rewards on this card\"\n3. Show the cost: \"Joining fee: ₹X (incl. GST). Your savings of ₹Y more than cover this in [Z] months\"\n4. Mention 2-3 relevant benefits (matched to their spending, not generic)\n\nFOR #2 AND #3 CARDS:\n• Brief comparison: \"If you prefer a lower fee, [Card #2] saves ₹X with no joining fee\"\n• Highlight the trade-off: \"You lose lounge access but save on fees\"\n\nALWAYS END WITH:\n• An offer to compare: \"Want me to compare the top 2 in detail?\"\n• Or a next step: \"Would you like to check if you're eligible for this card?\"\n• Or deeper info: \"Want to know more about the rewards structure?\"\n\nDO NOT:\n• List more than 3-4 cards (overwhelming)\n• Show raw numbers without context\n• Forget to explain WHY a card ranked where it did\n• Ignore the spending breakdown — it's your most powerful persuasion tool\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 10: LOOP PREVENTION & GUARDRAILS\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nSTRICT RULES to prevent getting stuck:\n\n1. NEVER ask the same question twice. Track what you've already asked in conversation.\n2. NEVER call recommend_cards more than 2 times with the same spending data.\n3. If the user says \"I don't know\" / \"skip\" / \"not sure\" for any category → set to 0, move on.\n4. If the user gives a vague answer after 2 clarification attempts → accept what you have and proceed.\n5. After showing recommendations, DO NOT restart spending collection unless the user explicitly says they want to change/add spending.\n6. If you have at least 2 categories with amounts → you CAN recommend. Don't keep asking forever.\n7. Maximum 4-5 questions before recommending. Respect the user's time.\n8. If the user seems impatient (\"just show me cards\") → recommend with whatever data you have.\n9. After each tool call, ALWAYS give a conversational response. Never go silent.\n10. If a tool returns an error → tell the user simply, suggest an alternative action.\n\nESCAPE HATCH:\nIf at ANY point the conversation feels stuck, say:\n\"Based on what you've told me so far, let me find the best cards for you.\"\nThen call recommend_cards with whatever spending data you have (set unknowns to 0).\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 11: TOOL SELECTION GUIDE\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nTOOL: recommend_cards\nWHEN: User has given spending amounts (even partial — at least 2 categories)\nHOW: Map all mentioned spending to correct keys. Set unmentioned categories to 0.\nFORMAT: Use \"full\" for first recommendation, \"brief\" for follow-ups\n\nTOOL: list_cards\nWHEN: User browses by category/feature, OR hasn't given spending data yet\nHOW: Map user intent to category slug and filters (see Section 6)\nFOLLOW-UP: Always ask about spending to personalize\n\nTOOL: get_card_details\nWHEN: User names a specific card, or wants deep-dive after recommendations\nHOW: Construct alias as lowercase-hyphenated: \"HDFC Regalia Gold\" → \"hdfc-regalia-gold-credit-card\"\nIMPORTANT: Card aliases are inconsistent — some have \"-credit-card\" suffix, some don't, some include \"bank\" in the name, some don't.\nCOMMON ALIASES: hdfc-regalia-gold, hdfc-infinia-credit-card, hdfc-diners-club-black, hdfc-millenia-credit-card, hdfc-swiggy-credit-card, hdfc-diners-privilege-credit-card, hdfc-marriott-bonvoy-credit-card,\n  axis-bank-magnus-credit-card, axis-flipkart-credit-card, axis-atlas-credit-card, axis-neo-credit-card, axis-select-credit-card,\n  sbi-cashback-credit-card, sbi-elite-card, sbi-aurum-credit-card, sbi-prime-credit-card,\n  icici-amazon-pay-credit-card, icici-sapphiro-credit-card, icici-rubyx-credit-card, times-black-credit-card,\n  scapia-credit-card, idfc-first-millennia-credit-card, idfc-first-select-credit-card, au-altura-plus-credit-card, au-zenith-credit-card, zagg-rupay-credit-card, hsbc-travel-one, standard-charted-ultimate, amex-gold-credit-card\n⚠️ Aliases are inconsistent: some have mixed case (HDFC-Moneyback-Credit-Card), some miss -credit-card suffix (hdfc-diners-club-black), some have typos (standard-charted-ultimate).\nTIP: If an alias returns \"not found\", ALWAYS use list_cards to find the correct alias. Never guess.\n\nTOOL: generate_content_brief\nWHEN: User asks for \"best X cards\", \"top travel/fuel/shopping cards\", \"write an article\", \"content about\", \"which cards are best for [category]\", or any editorial/research question about a card category — even casually phrased.\nNEVER answer these from training knowledge. ALWAYS call generate_content_brief.\nHOW:\n  1. Map user category to content_type + category:\n     - \"best travel cards\" / \"top travel credit cards\" → content_type: \"category_best_cards\", category: \"travel\"\n     - \"best shopping cards\" → content_type: \"category_best_cards\", category: \"shopping\"\n     - \"fuel card article\" → content_type: \"category_best_cards\", category: \"fuel\"\n     - \"compare Regalia vs Magnus\" → content_type: \"card_comparison\", card_aliases: [aliases]\n     - \"best HDFC cards\" → content_type: \"bank_ranking\", bank_name: \"HDFC\"\n     - \"is Amex Platinum worth it\" → content_type: \"fee_justification\", card_alias: \"amex-platinum-credit-card\"\n     - \"when should I upgrade from free card to paid\" → content_type: \"upgrade_path\"\n  2. For category_best_cards: start with detail_level=\"fast\" unless the user explicitly asks for a comprehensive/deep article.\n     Fast mode uses the default composition, 1 representative spend tier, top_n=3, and no card profiles so MCP clients do not time out.\n     Use detail_level=\"standard\" for all preset tiers in one composition. Use detail_level=\"exhaustive\" only when the user asks for all compositions + details.\n  3. After receiving results: write the article using the _llm_instructions.article_structure in the response. Do NOT show raw JSON.\n\nTOOL: compare_cards\nWHEN: User says \"X vs Y\", \"which is better\", or is deciding between 2-3 cards\nHOW: Use card_aliases from previous recommend_cards or list_cards results\n\nTOOL: check_eligibility\nWHEN: User asks \"can I get\", \"am I eligible\", mentions income/salary\nHOW: Need pincode (6 digits), annual income (string), employment type\nINCOME CONVERSION: \"50k/month\" → \"600000\", \"10 LPA\" → \"1000000\", \"1.5L/month\" → \"1800000\"\nEMPLOYMENT: salaried = any employer job, self_employed = freelancer/business/consultant\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSECTION 12: INDIAN CREDIT CARD DOMAIN KNOWLEDGE\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nFEES:\n• All card fees have 18% GST: ₹10,000 base = ₹11,800 actual\n• \"LTF\" = Lifetime Free = zero joining + zero annual fee forever\n• Many cards waive annual fee if you spend above a threshold (e.g., spend ₹2L/year → fee waived)\n\nREWARDS:\n• \"Reward points\" = most common. Value varies by card (1 point = ₹0.25 to ₹1.00)\n• \"Cashback\" = direct credit to statement (simpler, no conversion)\n• \"Miles\" = airline miles for travel cards (1 mile ≈ ₹0.75-₹1.50)\n• \"Accelerated rewards\" = higher earn rate on specific categories (e.g., 5x on dining)\n• \"Milestone benefits\" = bonus rewards when you hit annual spending targets\n\nLOUNGE ACCESS:\n• Domestic airport lounge: valued at ₹750/visit\n• International airport lounge: valued at ₹1,250/visit\n• Programs: Priority Pass, DreamFolks, individual bank lounge programs\n• Many cards give 2-8 complimentary domestic visits/quarter\n\nFUEL SURCHARGE:\n• Most fuel transactions have a 1% surcharge by default\n• Good fuel cards waive this surcharge (saves ₹100-200/month on ₹10K fuel spend)\n• Surcharge waiver usually has a cap (₹100-500/month)\n\nTOP BANKS & THEIR STRENGTHS:\n• HDFC: Best premium cards (Infinia, Diners Black), widest card range\n• SBI: Good value cards (Cashback, Elite), government-backed trust\n• ICICI: Strong co-brand cards (Amazon Pay, Sapphiro)\n• Axis: Good rewards (Magnus, Flipkart, Ace), Flipkart/Amazon partnerships\n• Kotak: Competitive mid-range cards\n• IDFC First: Best for beginners (Millennia, Classic)\n• AU Small Finance: Good entry-level (LIT card)\n• Amex: Best rewards but limited acceptance in India\n• RBL, IndusInd, Yes Bank: Niche premium cards\n• OneCard, Scapia, Fi: New-age digital-first cards\n\nCARD NETWORKS:\n• Visa: Widest acceptance globally and in India\n• Mastercard: Similar to Visa, slightly less acceptance\n• American Express (Amex): Best rewards and service, but ~70% acceptance in India\n• RuPay: Indian network, UPI linking, government cashback schemes, growing acceptance\n\nINCOME REQUIREMENTS (rough guide):\n• ₹3-5L annual: Entry cards (IDFC First, AU LIT, SBI SimplyCLICK)\n• ₹5-10L: Mid-range (HDFC Regalia, Axis Flipkart, SBI Cashback)\n• ₹10-15L: Premium (HDFC Regalia Gold, Axis Magnus, ICICI Sapphiro)\n• ₹15L+: Super-premium (HDFC Infinia, Diners Club Black, Axis Reserve)\n• ₹25L+: Ultra-premium (HDFC Infinia Metal, invite-only cards)\n",
  "_llm_instructions": {
    "how_to_use": [
      "This is your system-level operating manual for credit card advisory conversations.",
      "Internalize this context — it defines how you should behave for the rest of this session.",
      "The brand mappings (Section 3) are CRITICAL: they tell you which spending key to use when a user mentions a brand.",
      "The correlated pairs (Section 4) prevent you from missing related spending categories.",
      "The guardrails (Section 10) prevent infinite loops and stuck conversations."
    ],
    "important": "You do NOT need to call this tool again during this session. The context is persistent — use it for all subsequent tool calls.",
    "other_tools_available": {
      "generate_content_brief": {
        "when": "User asks for \"best X cards\", \"top travel/fuel/shopping cards\", \"write an article\", \"content ideas\", \"which cards are best for [category]\", \"carousel about\", \"blog post about\", or ANY editorial/research question about cards — even casually phrased.",
        "rule": "NEVER answer category or content questions from training knowledge. ALWAYS call generate_content_brief.",
        "params": "content_type (category_best_cards | card_comparison | persona_guide | upgrade_path | fee_justification | bank_ranking) + category or card_aliases as needed. Default detail_level=\"fast\"; use \"standard\" or \"exhaustive\" only when the user asks for deeper research. Optional: output_format (blog|carousel|reels|thread|linkedin), audience, goal, hook, tone."
      },
      "run_api_diagnostics": {
        "when": "Use for API QA, deployment checks, schema drift, latency debugging, or when an MCP/API call seems flaky.",
        "params": "scope=\"quick\" for core checks; scope=\"full\" for category listing and eligibility too. include_samples=true when debugging response shape."
      }
    }
  },
  "_integration_hint": "For chatbot developers: call this tool ONCE at session start and inject the \"context\" field into your system prompt. This gives your LLM the full advisory playbook without needing to call it per-turn."
}
```
</details>

<details><summary>recommend_cards {"grocery_spends_online": 20000, "fuel": 5000, "top_n": 3, "response_format": "full"}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "SBI CASHBACK ",
      "bank_name": "SBI",
      "card_type": "VISA",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-cashback-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945"
    },
    {
      "rank": 2,
      "card_name": "HSBC Live+ Credit Card",
      "bank_name": "HSBC Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 35,
          "brands": [],
          "card_id": 50,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "20000",
          "voucher_bonus": "1000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 1000
        },
        {
          "id": 36,
          "brands": [
            {
              "id": 14,
              "name": "Amazon"
            }
          ],
          "card_id": 50,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "0",
          "voucher_bonus": "250",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 250
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "hsbc-live-plus-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122030_AGB_Mockup-22.webp1735897902637"
    },
    {
      "rank": 3,
      "card_name": "PhonePe SBI Card SELECT BLACK ",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "Free (waived at ₹3,00,000/yr spend; ₹1,769 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 163,
          "brands": [
            {
              "id": 160,
              "name": "PhonePe App"
            }
          ],
          "card_id": 183,
          "rp_bonus": "",
          "maximum_days": "45",
          "minimum_spend": "100",
          "voucher_bonus": "1500",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "First transaction of minimum Rs. 100 within 30 days of card issuance to activate card and become eligible for voucher",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "electricity_bills",
          "annual_value": "₹0"
        },
        {
          "category": "water_bills",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "phonepe-sbi-card-select-black",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-cashback-credit-card"}</summary>

```
{
  "name": "SBI Cashback Credit Card",
  "nick_name": "SBI Cashback,Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4,
  "user_ratings": 413,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": false,
  "existing_customer_only": true,
  "fees": {
    "joining": "₹1,179 (₹999 + GST)",
    "joining_note": "A one-time joining fee is charged at the time of card issuance as per the bank’s policy.",
    "annual": "₹1,179 (₹999 + GST)",
    "annual_note": "The annual fee is charged every year and may be waived if you meet the bank’s spending conditions.",
    "annual_fee_waiver": "The annual fee is waived if you spend ₹2 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.50%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.50%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card (minimum ₹500, if applicable)",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹250",
    "reward_redemption_fee": "Not Applicable",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1001 - ₹10000",
        "fee": "₹ 750"
      },
      {
        "outstanding": "₹10000 - ₹25000",
        "fee": "₹ 950"
      },
      {
        "outstanding": "₹25001- ₹ 50000",
        "fee": "₹ 1100"
      },
      {
        "outstanding": "₹50000 and above",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared",
    "tnc_url": "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/ekit-tncs/cashback-tnc-ekit.pdf"
  },
  "rewards": {
    "point_value": null,
    "redemption_options": "This is a cashback card, and the earned cashback is adjusted directly in your monthly statement.",
    "redemption_catalogue": null,
    "exclusions": "Fuel Transactions, Rent Payments, Wallet Loads, Cash Withdrawals, EMI Transactions, Fees & Charges, Government Payments, Education Payments, Insurance Premium Payments, Utility Bills Payments, Gift Card or Voucher Purchases, Reversed or Refunded Transactions, Gaming Platforms, Tolls",
    "exclusion_spends": "Fuel Transactions, Rent Payments, Wallet Loads, Cash Withdrawals, EMI Transactions, Fees & Charges, Government Payments, Education Payments, Insurance Premium Payments, Utility Bills Payments, Gift Card or Voucher Purchases, Reversed or Refunded Transactions, Gaming Platforms, Tolls"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 60000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Get 5% Cashback on Dining",
      "description": "Restaurant Payments processed through online platforms using the SBI Cashback Credit Card"
    },
    {
      "title": "Earn 5% Cashback on Online Spends",
      "description": "capped at ₹2,000 and 1% on offline spends capped at ₹2,000 every statement cycle, with a total cashback of up to ₹4,000 per billing cycle"
    },
    {
      "title": "Get 5% Cashback on",
      "description": "Blinkit, Zepto, BigBasket, Instamart with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 5% Cashback on Food Orders",
      "description": "on all online food orders, making every meal more rewarding with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 5% Cashback",
      "description": "on all online shopping spends including Amazon, Flipkart, Myntra, Ajio, and many more with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 1% Cashback",
      "description": "on grocery shopping at departmental stores (offline merchants) using the SBI Cashback Credit Card with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get Flat 1% Cashback",
      "description": "on all offline spends with a capping of ₹2,000 per statement cycle (including the online spends)"
    }
  ],
  "tags": [
    "Shopping",
    "Online Food Ordering",
    "Dining",
    "Grocery Shopping"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• 5% cashback on online spends\n• Maximum online cashback of ₹2,000 per statement cycle\n• 1% cashback on offline spends\n• Maximum offline cashback of ₹2,000 per statement cycle; total cashback capped at ₹4,000 per statement cycle\n• Annual fee reversal on annual spends of ₹2 lakh"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Get 5% Cashback on Dining restaurant payments processed through online platform using the SBI Cashback Credit Card"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• Get a 1% fuel surcharge waiver for transactions between ₹500 and ₹3,000, with a maximum waiver of ₹100 per billing cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offers",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 65,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 30000,
    "crif_salaried": 750,
    "crif_self_emp": 750
  },
  "card_alias": "sbi-cashback-credit-card"
}
```
</details>

<details><summary>get_card_details {"card_alias": "hsbc-live-plus-credit-card"}</summary>

```
{
  "name": "HSBC Live Plus Credit Card",
  "nick_name": "HSBC Live Plus, Credit Card",
  "bank": "HSBC Bank",
  "bank_id": 12,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4,
  "user_ratings": 300,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122030_AGB_Mockup-22.webp1735897902637",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "salaried",
  "new_to_credit": true,
  "existing_customer_only": true,
  "fees": {
    "joining": "₹1,179 (₹999 + GST)",
    "joining_note": "A one-time joining fee of ₹999 is charged at the time of card issuance as per the bank's policy.",
    "annual": "₹1,179 (₹999 + GST)",
    "annual_note": "The annual fee is charged every year and may be waived if you meet the bank's spending conditions.",
    "annual_fee_waiver": "The annual fee is waived if you spend ₹200000 or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.50%",
    "forex_markup_note": "3.50% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.50%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card, subject to a minimum of ₹500.",
    "railway_surcharge": "1.80%",
    "railway_surcharge_note": "A railway booking surcharge of 1.80% for online transactions and 2.50% for other bookings is applied, with additional bank charges and taxes recovered at actuals.",
    "rent_payment_fee": "1%",
    "cash_payment_fee": "₹100",
    "cheque_payment_fee": "₹500",
    "reward_redemption_fee": "Not Applicable",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹5000",
        "fee": "₹500"
      },
      {
        "outstanding": "₹5001 - ₹10000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10001- and above",
        "fee": "₹1200"
      }
    ],
    "late_payment_note": "Late payment charges apply if the Minimum Amount Due (MAD) is not paid by the due date. Charges are based on the total outstanding amount as per the slab structure above.",
    "tnc_url": "https://www.hsbc.co.in/content/dam/hsbc/in/documents/most-important-terms-and-conditions.pdf"
  },
  "rewards": {
    "point_value": null,
    "redemption_options": "This is a cashback card, and the earned cashback is adjusted directly in your monthly statement.",
    "redemption_catalogue": null,
    "exclusions": "Utilities, Wallet loads, Fuel, Property management fees, Rent payments, Insurance premiums, Education, Government payments, Toll, Casino/gambling, Money transfers, EMI transactions, Business services, Security brokers, Jewellery, Charity, Wholesale clubs, Card repayments, Foreign currency, Cash withdrawal.",
    "exclusion_spends": "Utilities, Wallet loads, Fuel, Property management fees, Rent payments, Insurance premiums, Education, Government payments, Toll, Casino/gambling, Money transfers, EMI transactions, Business services, Security brokers, Jewellery, Charity, Wholesale clubs, Card repayments, Foreign currency, Cash withdrawa"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 30000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Earn 10% Cashback on Dining",
      "description": "capped at ₹1,000 per month"
    },
    {
      "title": "Earn 10% Cashback on Food Delivery",
      "description": "capped at ₹1,000 per month"
    },
    {
      "title": "Earn 10% Cashback on Grocery Shopping",
      "description": "capped at ₹1,000 per month"
    },
    {
      "title": "Earn 1.5% Unlimited Cashback on Shopping",
      "description": "& on most other retail categories with no monthly cap"
    },
    {
      "title": "Earn 1.5% Unlimited Cashback on Hotels",
      "description": "& on most other retail categories with no monthly cap"
    },
    {
      "title": "Get ₹1,000 Cashback on Spending ₹20,000",
      "description": "in the first 30 days plus ₹250 Amazon eGift Voucher on online application with video verification"
    },
    {
      "title": "Get 4 Complimentary Domestic Airport Lounge",
      "description": "visits per year maximum 1 visit per calendar quarter"
    }
  ],
  "tags": [
    "Shopping",
    "Online Food Ordering",
    "Dining",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• Earn 10% cashback on dining, food delivery, and grocery spends, one of the highest cashback rates in these everyday categories, capped at ₹1,000/month\n• Get 1.5% unlimited cashback with no monthly cap on shopping, hotels, medicine, and most other retail spends\n• Welcome package worth ₹1,250 - ₹1,000 cashback on ₹20,000 spend in 30 days plus ₹250 Amazon voucher on online application"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Get ₹1,000 cashback as statement credit on spending ₹20,000 within the first 30 days, requires downloading and logging into the HSBC India Mobile Banking app\n• Get ₹250 Amazon eGift Voucher on applying online, completing video verification, and receiving the card"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• 4 complimentary domestic airport lounge visits per year, maximum 1 visit per calendar quarter"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Benefits",
      "details": "• 1.5% unlimited cashback applicable on movie and entertainment spends"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• 10% cashback on dining and food delivery spends, capped at ₹1,000 per month (shared cap across dining, food delivery, and grocery)"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Surcharge Waiver Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offers",
      "details": "• 10% cashback on grocery spends, capped at ₹1,000 per month (shared cap with dining and food delivery)\n• 1.5% unlimited cashback on shopping, hotels, medicine, and most other retail categories, no monthly cap\n• Annual fee of ₹999 waived on spending ₹2,00,000 in a card year"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 65,
    "income_salaried_lpa": 6,
    "income_self_emp_lpa": 6,
    "min_income_monthly": 50000,
    "crif_salaried": 720,
    "crif_self_emp": 725
  },
  "card_alias": "hsbc-live-plus-credit-card"
}
```
</details>

<details><summary>get_card_details {"card_alias": "phonepe-sbi-card-select-black"}</summary>

```
{
  "name": "PhonePe SBI Card SELECT BLACK ",
  "nick_name": "Phonepe SBI SELECT BLACK, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.1,
  "user_ratings": 337,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": true,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "The annual fee is waived if you spend ₹3 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card (minimum ₹500, if applicable)",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹200",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1001 - ₹10000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10001 - ₹25000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25001 - ₹50000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared",
    "tnc_url": "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/most-important-terms-and-conditions/mitc-english.pdf"
  },
  "rewards": {
    "point_value": "1 Reward Points = ₹1",
    "redemption_options": "• SBI Reward Portal\n• Product\n• Vouchers",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, e-wallet, rent, property management, school and education services, government spends, digital gaming, financial charges, Encash, disputed transactions, ATM withdrawals, Flexipay transactions and merchant EMI spends",
    "exclusion_spends": "Fuel, e-wallet, rent, property management, school and education services, government spends, digital gaming, financial charges, Encash, disputed transactions, ATM withdrawals, Flexipay transactions and merchant EMI spends"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 44400,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Get Yatra Voucher on Annual",
      "description": "spends of Rs. 5 lakh with a Yatra e-Voucher worth Rs. 5,000 valid for 4 months"
    },
    {
      "title": "Earn 10 Rewards per ₹100",
      "description": "on eligible PhonePe spends"
    }
  ],
  "tags": [
    "Shopping",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• 10 reward points per ₹100 on eligible PhonePe spends\n• 5 reward points per ₹100 on eligible online spends\n• PhonePe e-Gift Card worth ₹1,500 on payment of annual fee ₹1,499"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• PhonePe e-Gift Card worth ₹1,500 on payment of annual fee ₹1,499"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• Yatra e-Voucher worth ₹5,000 on annual spends of ₹5 lakh\n• Valid for domestic/international flights, hotels, and holidays\n• Voucher valid for 4 months and usable in a single transaction"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• 4 complimentary domestic lounge visits per year (max 1 per quarter)"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Wavier Benefits",
      "details": "• 1% fuel surcharge waiver on transactions between ₹500–₹4,000 at petrol pumps across India\n• Maximum waiver of ₹250 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 70,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25000,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "phonepe-sbi-card-select-black"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q2 run 2 [everyday]
**What to check:** Fuel/grocery exclusions and caps: does the bot mention them from card terms, or ignore them?

**User:** I spend about 20,000 a month on groceries and 5,000 on fuel. Best cashback card for me?

**Bot:** Based on your spending, the **SBI CashBack Credit Card** saves you **₹12,000** per year. Your **₹20,000/month** grocery spending earns rewards and adds substantial savings.

- **Joining fee:** ₹1,179 (incl. GST)
- **Annual fee:** Free (waived at ₹2,00,000 annual spend; ₹1,179 otherwise)

### Key Benefits:
- Earns 5% cashback on grocery spends.
- Cashback value of **₹12,000** for the year.

![SBI CashBack Credit Card](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945)

### Caveat:
This card has a joining fee, but the annual fee is waived if you spend over ₹2,00,000 in a year.

Check the bank's current terms before applying; approval is the bank's decision.

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI CASHBACK: joining fee ₹1,179 (incl. GST)).
Note from the card details tool: SBI Cashback Credit Card is marked existing customers only.
Note from the card details tool: SBI Cashback Credit Card lists 'Fuel Transactions' under rewards exclusions, so your fuel spend may earn nothing on this card.

<details><summary>recommend_cards {"grocery_spends_online": 20000, "fuel": 5000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "SBI CASHBACK ",
      "bank_name": "SBI",
      "card_type": "VISA",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-cashback-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945"
    },
    {
      "rank": 2,
      "card_name": "HSBC Live+ Credit Card",
      "bank_name": "HSBC Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 35,
          "brands": [],
          "card_id": 50,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "20000",
          "voucher_bonus": "1000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 1000
        },
        {
          "id": 36,
          "brands": [
            {
              "id": 14,
              "name": "Amazon"
            }
          ],
          "card_id": 50,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "0",
          "voucher_bonus": "250",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 250
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "hsbc-live-plus-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122030_AGB_Mockup-22.webp1735897902637"
    },
    {
      "rank": 3,
      "card_name": "PhonePe SBI Card SELECT BLACK ",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹12,000",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "Free (waived at ₹3,00,000/yr spend; ₹1,769 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 163,
          "brands": [
            {
              "id": 160,
              "name": "PhonePe App"
            }
          ],
          "card_id": 183,
          "rp_bonus": "",
          "maximum_days": "45",
          "minimum_spend": "100",
          "voucher_bonus": "1500",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "First transaction of minimum Rs. 100 within 30 days of card issuance to activate card and become eligible for voucher",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "electricity_bills",
          "annual_value": "₹0"
        },
        {
          "category": "water_bills",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "phonepe-sbi-card-select-black",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png"
    },
    {
      "rank": 4,
      "card_name": "BOB Cashback Credit Card",
      "bank_name": "Bank of Baroda",
      "card_type": "Mastercard",
      "net_annual_savings": "₹11,411",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹589 (incl. GST)",
      "annual_fee": "₹589 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "bob-cashback-credit-card",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130247_BankKaro_20260507_124725695_Mockup_1.png"
    },
    {
      "rank": 5,
      "card_name": "CRED IndusInd Bank Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "RuPay",
      "net_annual_savings": "₹11,411",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "₹589 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "grocery_spends_online",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "cred-indusind-bank-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260625_173501453_Mockup_45.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-cashback-credit-card"}</summary>

```
{
  "name": "SBI Cashback Credit Card",
  "nick_name": "SBI Cashback,Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4,
  "user_ratings": 413,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": false,
  "existing_customer_only": true,
  "fees": {
    "joining": "₹1,179 (₹999 + GST)",
    "joining_note": "A one-time joining fee is charged at the time of card issuance as per the bank’s policy.",
    "annual": "₹1,179 (₹999 + GST)",
    "annual_note": "The annual fee is charged every year and may be waived if you meet the bank’s spending conditions.",
    "annual_fee_waiver": "The annual fee is waived if you spend ₹2 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.50%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.50%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card (minimum ₹500, if applicable)",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹250",
    "reward_redemption_fee": "Not Applicable",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1001 - ₹10000",
        "fee": "₹ 750"
      },
      {
        "outstanding": "₹10000 - ₹25000",
        "fee": "₹ 950"
      },
      {
        "outstanding": "₹25001- ₹ 50000",
        "fee": "₹ 1100"
      },
      {
        "outstanding": "₹50000 and above",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared",
    "tnc_url": "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/ekit-tncs/cashback-tnc-ekit.pdf"
  },
  "rewards": {
    "point_value": null,
    "redemption_options": "This is a cashback card, and the earned cashback is adjusted directly in your monthly statement.",
    "redemption_catalogue": null,
    "exclusions": "Fuel Transactions, Rent Payments, Wallet Loads, Cash Withdrawals, EMI Transactions, Fees & Charges, Government Payments, Education Payments, Insurance Premium Payments, Utility Bills Payments, Gift Card or Voucher Purchases, Reversed or Refunded Transactions, Gaming Platforms, Tolls",
    "exclusion_spends": "Fuel Transactions, Rent Payments, Wallet Loads, Cash Withdrawals, EMI Transactions, Fees & Charges, Government Payments, Education Payments, Insurance Premium Payments, Utility Bills Payments, Gift Card or Voucher Purchases, Reversed or Refunded Transactions, Gaming Platforms, Tolls"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 60000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Get 5% Cashback on Dining",
      "description": "Restaurant Payments processed through online platforms using the SBI Cashback Credit Card"
    },
    {
      "title": "Earn 5% Cashback on Online Spends",
      "description": "capped at ₹2,000 and 1% on offline spends capped at ₹2,000 every statement cycle, with a total cashback of up to ₹4,000 per billing cycle"
    },
    {
      "title": "Get 5% Cashback on",
      "description": "Blinkit, Zepto, BigBasket, Instamart with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 5% Cashback on Food Orders",
      "description": "on all online food orders, making every meal more rewarding with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 5% Cashback",
      "description": "on all online shopping spends including Amazon, Flipkart, Myntra, Ajio, and many more with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get 1% Cashback",
      "description": "on grocery shopping at departmental stores (offline merchants) using the SBI Cashback Credit Card with a capping of ₹2,000 per statement cycle"
    },
    {
      "title": "Get Flat 1% Cashback",
      "description": "on all offline spends with a capping of ₹2,000 per statement cycle (including the online spends)"
    }
  ],
  "tags": [
    "Shopping",
    "Online Food Ordering",
    "Dining",
    "Grocery Shopping"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• 5% cashback on online spends\n• Maximum online cashback of ₹2,000 per statement cycle\n• 1% cashback on offline spends\n• Maximum offline cashback of ₹2,000 per statement cycle; total cashback capped at ₹4,000 per statement cycle\n• Annual fee reversal on annual spends of ₹2 lakh"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Get 5% Cashback on Dining restaurant payments processed through online platform using the SBI Cashback Credit Card"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• Get a 1% fuel surcharge waiver for transactions between ₹500 and ₹3,000, with a maximum waiver of ₹100 per billing cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offers",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 65,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 30000,
    "crif_salaried": 750,
    "crif_self_emp": 750
  },
  "card_alias": "sbi-cashback-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q3 run 1 [mixed monthly/annual]
**What to check:** Unit handling: monthly vs annual passed correctly? Insurance often excluded from rewards.

**User:** Monthly I spend 25k on Swiggy/Zomato and 10k on Amazon. Yearly I spend 1.2 lakh on travel and 60k on insurance premium. Which card gives me the highest net savings?

**Bot:** Based on your spending, the **SBI Landmark Reward SELECT Credit Card** saves you **₹33,631** per year. Here's why it's the top pick for you:

- Your **₹25,000/month** spend on food delivery (Swiggy/Zomato) earns rewards.
- Your **₹10,000/month** spend on Amazon also contributes to significant rewards.
- Joining fee: **₹1,769** (including GST), and no waiver available.

**Benefits:**
- Annual rewards value: **₹5,400**.
- Additional milestone benefits of **₹30,000**.
- User rating: **4.2**.

![SBI Landmark Reward SELECT Credit Card](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png)

### Other Options:
1. **ixigo AU Credit Card**: Net savings of **₹33,500**. Joining fee is **free**.
2. **PhonePe SBI Card SELECT BLACK**: Net savings of **₹29,000**. Joining fee of **₹1,769** (waived at a spend of ₹3,00,000/year).

Would you like to know more about the second or third card? Or do you want to check your eligibility for the SBI card?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI Landmark Reward SELECT Credit Card: joining fee ₹1,769 (incl. GST); PhonePe SBI Card SELECT BLACK: joining fee ₹1,769 (incl. GST)).
Note from the card details tool: PhonePe SBI Card SELECT BLACK is marked existing customers only.

<details><summary>recommend_cards {"online_food_ordering": 25000, "amazon_spends": 10000, "flights_annual": 120000, "insurance_health_annual": 60000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹33,631",
      "annual_rewards_value": "₹5,400",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹250"
        },
        {
          "category": "online_food_ordering",
          "annual_value": "₹125"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹50"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 2,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹33,500",
      "annual_rewards_value": "₹13,500",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹625"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹250"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹250"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    },
    {
      "rank": 3,
      "card_name": "PhonePe SBI Card SELECT BLACK ",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹29,000",
      "annual_rewards_value": "₹24,000",
      "milestone_benefits": "₹5,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "Free (waived at ₹3,00,000/yr spend; ₹1,769 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 163,
          "brands": [
            {
              "id": 160,
              "name": "PhonePe App"
            }
          ],
          "card_id": 183,
          "rp_bonus": "",
          "maximum_days": "45",
          "minimum_spend": "100",
          "voucher_bonus": "1500",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "First transaction of minimum Rs. 100 within 30 days of card issuance to activate card and become eligible for voucher",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹500"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹500"
        }
      ],
      "card_alias": "phonepe-sbi-card-select-black",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png"
    },
    {
      "rank": 4,
      "card_name": "SBI CASHBACK ",
      "bank_name": "SBI",
      "card_type": "VISA",
      "net_annual_savings": "₹27,000",
      "annual_rewards_value": "₹27,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹1,250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹500"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹500"
        }
      ],
      "card_alias": "sbi-cashback-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945"
    },
    {
      "rank": 5,
      "card_name": "IndusInd Tiger Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹26,000",
      "annual_rewards_value": "₹6,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹100"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹100"
        }
      ],
      "card_alias": "indusind-tiger-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125059_BankKaro_Mockup_Desktop_1.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-landmark-reward-select-credit-card"}</summary>

```
{
  "name": "SBI Landmark Reward SELECT Credit Card",
  "nick_name": "SBI Landmark Reward SELECT, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.2,
  "user_ratings": 449,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "Not Applicable",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.50% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currencyExamples (3.5%):₹100 → ₹3.50₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.50% of the withdrawn amount is charged on cash advances using the credit card minimum ₹500, if applicable",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1,000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1,001 - ₹10,000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10,001 - ₹25,000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25,001 - ₹50,000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50,000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "An additional ₹100 applies if the Minimum Amount Due is not paid for two consecutive billing cycles",
    "tnc_url": "https://www.sbicard.com/en/most-important-terms-and-conditions.page"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.25",
    "redemption_options": "• Gift Vouchers\n• Merchandise&nbsp;",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI",
    "exclusion_spends": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 10000,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Earn 15 Reward Points per ₹100 Spent at Online and Retail Landmark Stores",
      "description": "Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy all earn the accelerated rate, with no monthly or annual earning cap"
    },
    {
      "title": "Earn 10 Reward Points per ₹100 Spent on",
      "description": "restaurant bills, movie ticket spends and all international transaction"
    }
  ],
  "tags": [
    "Shopping",
    "Dining"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• earn 15 Reward Points per ₹100 spent at online and retail Landmark Stores Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy\n• 10 Reward Points per ₹100 spent on dining, movies and international spends\n• The milestone benefit gives 12,000 bonus Reward Points on overall annual retail spends of ₹3,00,000\n• Reward Points can also be converted into Landmark Rewards at 2.4 Reward Points = 1 LMR, with 1 LMR = ₹0.60"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Get 6,000 bonus Reward Points worth ₹1,500 on payment of the annual fee"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on movies"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on dining"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver at all petrol pumps across India, on transactions between ₹500 and ₹3,000. Maximum waiver of ₹100 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25001,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "sbi-landmark-reward-select-credit-card"
}
```
</details>

<details><summary>get_card_details {"card_alias": "phonepe-sbi-card-select-black"}</summary>

```
{
  "name": "PhonePe SBI Card SELECT BLACK ",
  "nick_name": "Phonepe SBI SELECT BLACK, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.1,
  "user_ratings": 337,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": true,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "The annual fee is waived if you spend ₹3 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card (minimum ₹500, if applicable)",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹200",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1001 - ₹10000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10001 - ₹25000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25001 - ₹50000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared",
    "tnc_url": "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/most-important-terms-and-conditions/mitc-english.pdf"
  },
  "rewards": {
    "point_value": "1 Reward Points = ₹1",
    "redemption_options": "• SBI Reward Portal\n• Product\n• Vouchers",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, e-wallet, rent, property management, school and education services, government spends, digital gaming, financial charges, Encash, disputed transactions, ATM withdrawals, Flexipay transactions and merchant EMI spends",
    "exclusion_spends": "Fuel, e-wallet, rent, property management, school and education services, government spends, digital gaming, financial charges, Encash, disputed transactions, ATM withdrawals, Flexipay transactions and merchant EMI spends"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 44400,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Get Yatra Voucher on Annual",
      "description": "spends of Rs. 5 lakh with a Yatra e-Voucher worth Rs. 5,000 valid for 4 months"
    },
    {
      "title": "Earn 10 Rewards per ₹100",
      "description": "on eligible PhonePe spends"
    }
  ],
  "tags": [
    "Shopping",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• 10 reward points per ₹100 on eligible PhonePe spends\n• 5 reward points per ₹100 on eligible online spends\n• PhonePe e-Gift Card worth ₹1,500 on payment of annual fee ₹1,499"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• PhonePe e-Gift Card worth ₹1,500 on payment of annual fee ₹1,499"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• Yatra e-Voucher worth ₹5,000 on annual spends of ₹5 lakh\n• Valid for domestic/international flights, hotels, and holidays\n• Voucher valid for 4 months and usable in a single transaction"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• 4 complimentary domestic lounge visits per year (max 1 per quarter)"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Wavier Benefits",
      "details": "• 1% fuel surcharge waiver on transactions between ₹500–₹4,000 at petrol pumps across India\n• Maximum waiver of ₹250 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 70,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25000,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "phonepe-sbi-card-select-black"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q3 run 2 [mixed monthly/annual]
**What to check:** Unit handling: monthly vs annual passed correctly? Insurance often excluded from rewards.

**User:** Monthly I spend 25k on Swiggy/Zomato and 10k on Amazon. Yearly I spend 1.2 lakh on travel and 60k on insurance premium. Which card gives me the highest net savings?

**Bot:** Based on your spending, the **SBI Landmark Reward SELECT Credit Card** offers the highest net annual savings of **₹33,631**. Here's why it's the top pick for you:

- Your **₹10,000/month** Amazon spend and **₹25,000/month** on food delivery earned you significant rewards.
- The card provides an **annual rewards value** of **₹5,400**.
- Additionally, it has milestone benefits worth **₹30,000**.

### Cost Breakdown:
- **Joining fee**: ₹1,769 (incl. GST)
- **Annual fee**: ₹1,769 (incl. GST) which is not waived.

### Benefits:
- Welcome benefits include **6,000 reward points** (valued at ₹1,500).
- User rating: **4.2** out of 5.

![SBI Landmark Reward SELECT Credit Card](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png)

If you're interested in other options, the **ixigo AU Credit Card** offers a similar net annual savings of **₹33,500**, with no joining or annual fee, but lower overall rewards.

Would you like to compare the top two cards in detail or check eligibility for the SBI card?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI Landmark Reward SELECT Credit Card: joining fee ₹1,769 (incl. GST)).

<details><summary>recommend_cards {"online_food_ordering": 25000, "amazon_spends": 10000, "flights_annual": 120000, "insurance_health_annual": 60000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹33,631",
      "annual_rewards_value": "₹5,400",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹250"
        },
        {
          "category": "online_food_ordering",
          "annual_value": "₹125"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹50"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 2,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹33,500",
      "annual_rewards_value": "₹13,500",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹625"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹250"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹250"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    },
    {
      "rank": 3,
      "card_name": "PhonePe SBI Card SELECT BLACK ",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹29,000",
      "annual_rewards_value": "₹24,000",
      "milestone_benefits": "₹5,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "Free (waived at ₹3,00,000/yr spend; ₹1,769 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [
        {
          "id": 163,
          "brands": [
            {
              "id": 160,
              "name": "PhonePe App"
            }
          ],
          "card_id": 183,
          "rp_bonus": "",
          "maximum_days": "45",
          "minimum_spend": "100",
          "voucher_bonus": "1500",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "First transaction of minimum Rs. 100 within 30 days of card issuance to activate card and become eligible for voucher",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹500"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹500"
        }
      ],
      "card_alias": "phonepe-sbi-card-select-black",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130245_BankKaro_20260408_171510212_IDFC_FIRST_Indigo_Credit_Card_-mockup_9.png"
    },
    {
      "rank": 4,
      "card_name": "SBI CASHBACK ",
      "bank_name": "SBI",
      "card_type": "VISA",
      "net_annual_savings": "₹27,000",
      "annual_rewards_value": "₹27,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹1,179 (incl. GST)",
      "annual_fee": "Free (waived at ₹2,00,000/yr spend; ₹1,179 otherwise)",
      "annual_fee_waived": true,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹1,250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹500"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹500"
        }
      ],
      "card_alias": "sbi-cashback-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_122010_AGB_Mockup-24.webp1736921642945"
    },
    {
      "rank": 5,
      "card_name": "IndusInd Tiger Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹26,000",
      "annual_rewards_value": "₹6,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "online_food_ordering",
          "annual_value": "₹250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹100"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹100"
        }
      ],
      "card_alias": "indusind-tiger-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125059_BankKaro_Mockup_Desktop_1.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-landmark-reward-select-credit-card"}</summary>

```
{
  "name": "SBI Landmark Reward SELECT Credit Card",
  "nick_name": "SBI Landmark Reward SELECT, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.2,
  "user_ratings": 449,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "Not Applicable",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.50% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currencyExamples (3.5%):₹100 → ₹3.50₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.50% of the withdrawn amount is charged on cash advances using the credit card minimum ₹500, if applicable",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1,000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1,001 - ₹10,000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10,001 - ₹25,000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25,001 - ₹50,000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50,000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "An additional ₹100 applies if the Minimum Amount Due is not paid for two consecutive billing cycles",
    "tnc_url": "https://www.sbicard.com/en/most-important-terms-and-conditions.page"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.25",
    "redemption_options": "• Gift Vouchers\n• Merchandise&nbsp;",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI",
    "exclusion_spends": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 10000,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Earn 15 Reward Points per ₹100 Spent at Online and Retail Landmark Stores",
      "description": "Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy all earn the accelerated rate, with no monthly or annual earning cap"
    },
    {
      "title": "Earn 10 Reward Points per ₹100 Spent on",
      "description": "restaurant bills, movie ticket spends and all international transaction"
    }
  ],
  "tags": [
    "Shopping",
    "Dining"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• earn 15 Reward Points per ₹100 spent at online and retail Landmark Stores Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy\n• 10 Reward Points per ₹100 spent on dining, movies and international spends\n• The milestone benefit gives 12,000 bonus Reward Points on overall annual retail spends of ₹3,00,000\n• Reward Points can also be converted into Landmark Rewards at 2.4 Reward Points = 1 LMR, with 1 LMR = ₹0.60"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Get 6,000 bonus Reward Points worth ₹1,500 on payment of the annual fee"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on movies"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on dining"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver at all petrol pumps across India, on transactions between ₹500 and ₹3,000. Maximum waiver of ₹100 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25001,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "sbi-landmark-reward-select-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q4 run 1 [mixed monthly/annual]
**What to check:** 4 lakh/yr vs 8k/mo normalised consistently? Compare tool arguments with what the user said.

**User:** I spend 4 lakh a year on flights and 8,000 per month on dining out. What's best?

**Bot:** Based on your spending, the **Axis Bank Magnus Burgundy** card saves you **₹77,786/year**. This is ideal for you because:

- Your **₹4 lakh/year** flight spending earns high rewards.
- Dining out adds further value with an additional reward.

**Cost:**
- Joining fee: **₹35,400 (incl. GST)**.
- Annual fee: **₹35,400 (incl. GST)**; no waiver available.

### Benefits:
- **Welcome benefit**: ₹5,000 voucher (Postcard Hotels, Yatra).
- **User rating**: 4/5.

![Axis Bank Magnus Burgundy](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130226_BankKaro_20260202_181828409_Axis_Magnus.png)

**Caveat:** The annual fee is high, but your rewards can offset it substantially. 

Check the bank's current terms before applying; approval is the bank's decision. Would you like to see more options or get further details?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (Axis Bank Magnus Burgundy: joining fee ₹35,400 (incl. GST)).
Note from the card details tool: Axis Burgundy Magnus Credit Card is marked invite only.

<details><summary>recommend_cards {"flights_annual": 400000, "dining_or_going_out": 8000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "Axis Bank Magnus Burgundy",
      "bank_name": "Axis",
      "card_type": "VISA",
      "net_annual_savings": "₹77,786",
      "annual_rewards_value": "₹1,13,186.157",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹35,400 (incl. GST)",
      "annual_fee": "₹35,400 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 131,
          "brands": [
            {
              "id": 85,
              "name": "Postcard Hotels"
            },
            {
              "id": 102,
              "name": "Yatra"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 173,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "",
          "voucher_bonus": "5000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 5000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹9,000.18"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹432"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "magnus-burgundy-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130226_BankKaro_20260202_181828409_Axis_Magnus.png"
    },
    {
      "rank": 2,
      "card_name": "HDFC Diners Club Black Metal Edition",
      "bank_name": "HDFC",
      "card_type": "DinersClub",
      "net_annual_savings": "₹61,268",
      "annual_rewards_value": "₹73,068",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹11,800 (incl. GST)",
      "annual_fee": "₹11,800 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 49,
          "brands": [
            {
              "id": 31,
              "name": "Club Marriott"
            },
            {
              "id": 17,
              "name": "Amazon Prime"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 103,
          "rp_bonus": "",
          "maximum_days": "90",
          "minimum_spend": "150000",
          "voucher_bonus": "25000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 0
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹5,555.667"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹533.333"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "hdfc-diners-club-black-metal-credit-card",
      "rating": 3,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125405_BankKaro_HDFC_Dineer_Bc.png"
    },
    {
      "rank": 3,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹40,631",
      "annual_rewards_value": "₹12,400.2",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹833.35"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹200"
        },
        {
          "category": "other_online_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 4,
      "card_name": "AXIS MAGNUS",
      "bank_name": "Axis",
      "card_type": "VISA",
      "net_annual_savings": "₹35,555",
      "annual_rewards_value": "₹50,304.961",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹14,750 (incl. GST)",
      "annual_fee": "₹14,750 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 8,
          "brands": [
            {
              "id": 85,
              "name": "Postcard Hotels"
            },
            {
              "id": 102,
              "name": "Yatra"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 6,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "12500",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 12500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹4,000.08"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹192"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "axis-bank-magnus-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_121948_BankKaro_20260129_121658926_Axis_Magnus.png"
    },
    {
      "rank": 5,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹32,400",
      "annual_rewards_value": "₹12,400.2",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹833.35"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹200"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "magnus-burgundy-credit-card"}</summary>

```
{
  "name": "Axis Burgundy Magnus Credit Card",
  "nick_name": "Magnus Burgundy, Credit Card",
  "bank": "Axis",
  "bank_id": 1,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4,
  "user_ratings": 200,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130226_BankKaro_20260202_181828409_Axis_Magnus.png",
  "priority_tag": null,
  "invite_only": true,
  "employment_type": "both",
  "new_to_credit": false,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹35,400 (₹30,000 + GST)",
    "joining_note": "A one-time joining fee is charged at the time of card issuance as per the bank’s policy.",
    "annual": "₹35,400 (₹30,000 + GST)",
    "annual_note": "The annual fee is charged every year and may be waived if you meet the bank’s spending conditions.",
    "annual_fee_waiver": "The annual fee is waived if you spend ₹25 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3%",
    "apr_annual": "36.00%",
    "forex_markup": "2%",
    "forex_markup_note": "2% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (2%):₹100 → ₹2₹1,000 → ₹20₹10,000 → ₹200₹1,00,000 → ₹2,000",
    "atm_withdrawal_fee": null,
    "atm_withdrawal_note": "N/A",
    "railway_surcharge": "As prescribed by IRCTC / Indian Railways",
    "railway_surcharge_note": "Surcharge on booking or cancelling railway tickets will be levied as prescribed by IRCTC or Indian Railways and may vary based on their applicable charges.",
    "rent_payment_fee": "1%",
    "cash_payment_fee": "₹175",
    "cheque_payment_fee": null,
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹5000",
        "fee": "₹500"
      },
      {
        "outstanding": "₹5001 - ₹10000",
        "fee": "₹750"
      },
      {
        "outstanding": "Above ₹10,000",
        "fee": "₹1200"
      }
    ],
    "late_payment_note": "Late Payment Fee is based on the total amount due: Nil (&lt;₹500), ₹500 (₹501–₹5,000), ₹750 (₹5,001–₹10,000), ₹1,200 (&gt;₹10,000).&nbsp;Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared.",
    "tnc_url": "https://www.axis.bank.in/docs/default-source/default-document-library/mitc-credit-cards.pdf"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.20",
    "redemption_options": "• Airline &amp; Hotel Transfers\n• Travel EDGE Portal\n• Rewards Store &amp; Vouchers\n• Statement Credits",
    "redemption_catalogue": "https://edgerewards.axisbank.co.in/lms/",
    "exclusions": "Fuel Spends, Wallet Loads, Rent Payment, Utility Bill Payments, Government-related Transactions, Insurance Payments, Jewellery Purchases, Rewards Redemption, Cash Advances, Outstanding Payments",
    "exclusion_spends": "Fuel Spends, Wallet Loads, Rent Payment, Utility Bill Payments, Government-related Transactions, Insurance Payments, Jewellery Purchases, Rewards Redemption, Cash Advances, Outstanding Payments"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 100000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Superior Miles Conversion for Burgundy",
      "description": "earn 4 partner miles for every 5 EDGE Reward Points, delivering higher value compared to regular Magnus"
    },
    {
      "title": "Priority Pass with Guest Access",
      "description": "enjoy unlimited international lounge visits with 4 complimentary guest visits per year"
    },
    {
      "title": "Travel EDGE Rewards",
      "description": "earn 5X EDGE Reward Points on spends via the Travel EDGE portal on cumulative spends up to ₹2 lakh per calendar month"
    },
    {
      "title": "Airport Meet & Assist Services",
      "description": "provide 4 complimentary services per calendar year, including assistance with check-in, security, immigration, and porter services at select Indian airports"
    },
    {
      "title": "Rewarding Shopping Spends",
      "description": "earn 12 EDGE Reward Points per ₹200 on shopping spends up to ₹1.5 lakh per calendar month and 35 EDGE Reward Points per ₹200 on incremental spends above ₹1.5 lakh"
    },
    {
      "title": "Dining Delights Programme",
      "description": "lets you save up to 30% on dining, capped at ₹1,000 per bill, at 4,000+ partner restaurants across India"
    },
    {
      "title": "Unlimited Lounge Access",
      "description": "gives unlimited domestic and international airport lounge visits with complimentary Priority Pass membership, including 4 accompanying guest visits per year"
    },
    {
      "title": "Burgundy-Exclusive Welcome Benefit",
      "description": "lets you choose a Luxe Gift Card, Postcard Hotels voucher, Yatra voucher, or a one-way domestic flight ticket worth up to ₹5,000, applicable only for new Burgundy cardholders and not for upgrades"
    },
    {
      "title": "Accelerated Reward Earnings",
      "description": "earn 12 EDGE Reward Points per ₹200 on spends up to ₹1.5 lakh per calendar month and 35 EDGE Reward Points per ₹200 on incremental spends beyond ₹1.5 lakh, capped at the assigned credit limit plus ₹1.5 lakh per month"
    },
    {
      "title": "Higher Annual Miles Transfer Limit",
      "description": "allow transfer of up to 10 lakh EDGE Reward Points per calendar year across airline and hotel partners"
    }
  ],
  "tags": [
    "Shopping",
    "Dining",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• Earn 12 EDGE Reward Points per ₹200 on spends up to ₹1.5 lakh per month\n• Earn 35 EDGE Reward Points per ₹200 on incremental spends above ₹1.5 lakh\n• Convert rewards at 5 EDGE Points = 4 partner miles\n• Annual reward transfer limit of 10 lakh EDGE Reward Points\n• Earn 5X EDGE Reward Points on Travel EDGE bookings up to ₹2 lakh per month"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Welcome voucher or one-way domestic economy flight ticket worth up to ₹5,000\n• Choice of Luxe Gift Card, Postcard Hotels voucher, or Yatra voucher\n• Applicable only for new card issuance, not upgrades\n• First eligible spend within 30 days of card issuance\n• Benefit to be redeemed within 6 months of issuance"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• • 4 complimentary Airport Meet &amp; Assist services per calendar year (includes check-in, security, immigration, porter)\n• Valid for domestic &amp; international departures/arrivals at select airports\n• Earn 5X EDGE Reward Points on flight &amp; hotel bookings via Travel EDGE"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• Unlimited international lounge access via Priority Pass\n• Includes 4 complimentary guest visits per year\n• Unlimited domestic airport lounge access in India\n• Domestic lounge access requires ₹50,000 spend in previous 3 months\n• Spend condition waived for newly issued cards initially"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Up to 30% discount via Dining Delights programme, Maximum discount of ₹1,000 per bill, Valid at 4,000+ partner restaurants across India"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 18,
    "max_age": 70,
    "income_salaried_lpa": 24,
    "income_self_emp_lpa": 24,
    "min_income_monthly": 150000,
    "crif_salaried": 750,
    "crif_self_emp": 750
  },
  "card_alias": "magnus-burgundy-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q4 run 2 [mixed monthly/annual]
**What to check:** 4 lakh/yr vs 8k/mo normalised consistently? Compare tool arguments with what the user said.

**User:** I spend 4 lakh a year on flights and 8,000 per month on dining out. What's best?

**Bot:** Based on your spending, the **Axis Bank Magnus Burgundy** card saves you **₹77,786** per year. Your annual flight spend of ₹4 lakh earns you approximately **₹9,000** in rewards, and your ₹8,000 monthly dining out contributes an additional **₹432** in rewards.

- **Joining fee:** ₹35,400 (incl. GST).
- **Annual fee:** ₹35,400 (incl. GST).
- No fee waiver is available.

### Key Benefits:
- Welcome benefit of ₹5,000 when booking through Yatra or Postcard Hotels.
- Significant rewards on flights, which suits your spending pattern.

**Caveat:** The joining fee is substantial, and although the net savings are high, they do not fully offset the joining fee in the first year.

Check the bank's current terms before applying; approval is the bank's decision. Would you like to see more options or compare with another card?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (Axis Bank Magnus Burgundy: joining fee ₹35,400 (incl. GST)).
Note from the card details tool: Axis Burgundy Magnus Credit Card is marked invite only.
Note from the tool data: Axis Bank Magnus Burgundy: the category figure ₹432 is a per-month amount (the tool's yearly rewards value for this card is ₹1,13,186.157).

<details><summary>recommend_cards {"flights_annual": 400000, "dining_or_going_out": 8000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "Axis Bank Magnus Burgundy",
      "bank_name": "Axis",
      "card_type": "VISA",
      "net_annual_savings": "₹77,786",
      "annual_rewards_value": "₹1,13,186.157",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹35,400 (incl. GST)",
      "annual_fee": "₹35,400 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 131,
          "brands": [
            {
              "id": 85,
              "name": "Postcard Hotels"
            },
            {
              "id": 102,
              "name": "Yatra"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 173,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "",
          "voucher_bonus": "5000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 5000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹9,000.18"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹432"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "magnus-burgundy-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130226_BankKaro_20260202_181828409_Axis_Magnus.png"
    },
    {
      "rank": 2,
      "card_name": "HDFC Diners Club Black Metal Edition",
      "bank_name": "HDFC",
      "card_type": "DinersClub",
      "net_annual_savings": "₹61,268",
      "annual_rewards_value": "₹73,068",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹11,800 (incl. GST)",
      "annual_fee": "₹11,800 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 49,
          "brands": [
            {
              "id": 31,
              "name": "Club Marriott"
            },
            {
              "id": 17,
              "name": "Amazon Prime"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 103,
          "rp_bonus": "",
          "maximum_days": "90",
          "minimum_spend": "150000",
          "voucher_bonus": "25000",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 0
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹5,555.667"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹533.333"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "hdfc-diners-club-black-metal-credit-card",
      "rating": 3,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125405_BankKaro_HDFC_Dineer_Bc.png"
    },
    {
      "rank": 3,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹40,631",
      "annual_rewards_value": "₹12,400.2",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹833.35"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹200"
        },
        {
          "category": "other_online_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 4,
      "card_name": "AXIS MAGNUS",
      "bank_name": "Axis",
      "card_type": "VISA",
      "net_annual_savings": "₹35,555",
      "annual_rewards_value": "₹50,304.961",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "₹14,750 (incl. GST)",
      "annual_fee": "₹14,750 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 8,
          "brands": [
            {
              "id": 85,
              "name": "Postcard Hotels"
            },
            {
              "id": 102,
              "name": "Yatra"
            },
            {
              "id": null,
              "name": null
            }
          ],
          "card_id": 6,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "12500",
          "cash_conversion": "",
          "welcome_benefit_tooltip": null,
          "cash_value": 12500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹4,000.08"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹192"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "axis-bank-magnus-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_121948_BankKaro_20260129_121658926_Axis_Magnus.png"
    },
    {
      "rank": 5,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹32,400",
      "annual_rewards_value": "₹12,400.2",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "flights_annual",
          "annual_value": "₹833.35"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹200"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "magnus-burgundy-credit-card"}</summary>

```
{
  "name": "Axis Burgundy Magnus Credit Card",
  "nick_name": "Magnus Burgundy, Credit Card",
  "bank": "Axis",
  "bank_id": 1,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4,
  "user_ratings": 200,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130226_BankKaro_20260202_181828409_Axis_Magnus.png",
  "priority_tag": null,
  "invite_only": true,
  "employment_type": "both",
  "new_to_credit": false,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹35,400 (₹30,000 + GST)",
    "joining_note": "A one-time joining fee is charged at the time of card issuance as per the bank’s policy.",
    "annual": "₹35,400 (₹30,000 + GST)",
    "annual_note": "The annual fee is charged every year and may be waived if you meet the bank’s spending conditions.",
    "annual_fee_waiver": "The annual fee is waived if you spend ₹25 lakh or more in a year on your card, as per bank policy.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3%",
    "apr_annual": "36.00%",
    "forex_markup": "2%",
    "forex_markup_note": "2% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (2%):₹100 → ₹2₹1,000 → ₹20₹10,000 → ₹200₹1,00,000 → ₹2,000",
    "atm_withdrawal_fee": null,
    "atm_withdrawal_note": "N/A",
    "railway_surcharge": "As prescribed by IRCTC / Indian Railways",
    "railway_surcharge_note": "Surcharge on booking or cancelling railway tickets will be levied as prescribed by IRCTC or Indian Railways and may vary based on their applicable charges.",
    "rent_payment_fee": "1%",
    "cash_payment_fee": "₹175",
    "cheque_payment_fee": null,
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹5000",
        "fee": "₹500"
      },
      {
        "outstanding": "₹5001 - ₹10000",
        "fee": "₹750"
      },
      {
        "outstanding": "Above ₹10,000",
        "fee": "₹1200"
      }
    ],
    "late_payment_note": "Late Payment Fee is based on the total amount due: Nil (&lt;₹500), ₹500 (₹501–₹5,000), ₹750 (₹5,001–₹10,000), ₹1,200 (&gt;₹10,000).&nbsp;Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared.",
    "tnc_url": "https://www.axis.bank.in/docs/default-source/default-document-library/mitc-credit-cards.pdf"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.20",
    "redemption_options": "• Airline &amp; Hotel Transfers\n• Travel EDGE Portal\n• Rewards Store &amp; Vouchers\n• Statement Credits",
    "redemption_catalogue": "https://edgerewards.axisbank.co.in/lms/",
    "exclusions": "Fuel Spends, Wallet Loads, Rent Payment, Utility Bill Payments, Government-related Transactions, Insurance Payments, Jewellery Purchases, Rewards Redemption, Cash Advances, Outstanding Payments",
    "exclusion_spends": "Fuel Spends, Wallet Loads, Rent Payment, Utility Bill Payments, Government-related Transactions, Insurance Payments, Jewellery Purchases, Rewards Redemption, Cash Advances, Outstanding Payments"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 100000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Superior Miles Conversion for Burgundy",
      "description": "earn 4 partner miles for every 5 EDGE Reward Points, delivering higher value compared to regular Magnus"
    },
    {
      "title": "Priority Pass with Guest Access",
      "description": "enjoy unlimited international lounge visits with 4 complimentary guest visits per year"
    },
    {
      "title": "Travel EDGE Rewards",
      "description": "earn 5X EDGE Reward Points on spends via the Travel EDGE portal on cumulative spends up to ₹2 lakh per calendar month"
    },
    {
      "title": "Airport Meet & Assist Services",
      "description": "provide 4 complimentary services per calendar year, including assistance with check-in, security, immigration, and porter services at select Indian airports"
    },
    {
      "title": "Rewarding Shopping Spends",
      "description": "earn 12 EDGE Reward Points per ₹200 on shopping spends up to ₹1.5 lakh per calendar month and 35 EDGE Reward Points per ₹200 on incremental spends above ₹1.5 lakh"
    },
    {
      "title": "Dining Delights Programme",
      "description": "lets you save up to 30% on dining, capped at ₹1,000 per bill, at 4,000+ partner restaurants across India"
    },
    {
      "title": "Unlimited Lounge Access",
      "description": "gives unlimited domestic and international airport lounge visits with complimentary Priority Pass membership, including 4 accompanying guest visits per year"
    },
    {
      "title": "Burgundy-Exclusive Welcome Benefit",
      "description": "lets you choose a Luxe Gift Card, Postcard Hotels voucher, Yatra voucher, or a one-way domestic flight ticket worth up to ₹5,000, applicable only for new Burgundy cardholders and not for upgrades"
    },
    {
      "title": "Accelerated Reward Earnings",
      "description": "earn 12 EDGE Reward Points per ₹200 on spends up to ₹1.5 lakh per calendar month and 35 EDGE Reward Points per ₹200 on incremental spends beyond ₹1.5 lakh, capped at the assigned credit limit plus ₹1.5 lakh per month"
    },
    {
      "title": "Higher Annual Miles Transfer Limit",
      "description": "allow transfer of up to 10 lakh EDGE Reward Points per calendar year across airline and hotel partners"
    }
  ],
  "tags": [
    "Shopping",
    "Dining",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• Earn 12 EDGE Reward Points per ₹200 on spends up to ₹1.5 lakh per month\n• Earn 35 EDGE Reward Points per ₹200 on incremental spends above ₹1.5 lakh\n• Convert rewards at 5 EDGE Points = 4 partner miles\n• Annual reward transfer limit of 10 lakh EDGE Reward Points\n• Earn 5X EDGE Reward Points on Travel EDGE bookings up to ₹2 lakh per month"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Welcome voucher or one-way domestic economy flight ticket worth up to ₹5,000\n• Choice of Luxe Gift Card, Postcard Hotels voucher, or Yatra voucher\n• Applicable only for new card issuance, not upgrades\n• First eligible spend within 30 days of card issuance\n• Benefit to be redeemed within 6 months of issuance"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• • 4 complimentary Airport Meet &amp; Assist services per calendar year (includes check-in, security, immigration, porter)\n• Valid for domestic &amp; international departures/arrivals at select airports\n• Earn 5X EDGE Reward Points on flight &amp; hotel bookings via Travel EDGE"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• Unlimited international lounge access via Priority Pass\n• Includes 4 complimentary guest visits per year\n• Unlimited domestic airport lounge access in India\n• Domestic lounge access requires ₹50,000 spend in previous 3 months\n• Spend condition waived for newly issued cards initially"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Up to 30% discount via Dining Delights programme, Maximum discount of ₹1,000 per bill, Valid at 4,000+ partner restaurants across India"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 18,
    "max_age": 70,
    "income_salaried_lpa": 24,
    "income_self_emp_lpa": 24,
    "min_income_monthly": 150000,
    "crif_salaried": 750,
    "crif_self_emp": 750
  },
  "card_alias": "magnus-burgundy-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q5 run 1 [mixed monthly/annual]
**What to check:** Education/school-fee spends: rewards usually excluded or surcharged. Does the tool/bot say so?

**User:** My total spend is around 50k a month, mostly online shopping, plus 36,000 a year for school fees. Suggest a card.

**Bot:** Based on your spending, the **Ixigo AU Credit Card** saves you **₹35,000/year**. This card is free to join and has no annual fee.

### Key Benefits:
- **Annual Rewards Value:** ₹15,000
- **Milestone Benefits:** ₹20,000
- **User Rating:** 4.2/5

![Ixigo AU Credit Card](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png)

---

If you prefer something else, the **SBI Landmark Reward SELECT Credit Card** also offers good value, saving you **₹31,231/year** with an **annual fee of ₹1,769 (incl. GST)**. 

### Key Benefits:
- **Annual Rewards Value:** ₹3,000
- **Milestone Benefits:** ₹30,000
- **User Rating:** 4.2/5

![SBI Landmark Reward SELECT](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png)

---

Check the bank's current terms before applying; approval is the bank's decision. Would you like to know more about either card?

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI Landmark Reward SELECT Credit Card: joining fee ₹1,769 (incl. GST)).

<details><summary>recommend_cards {"other_online_spends": 50000, "school_fees": 3000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹35,000",
      "annual_rewards_value": "₹15,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹1,250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "all_pharmacy",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    },
    {
      "rank": 2,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹31,231",
      "annual_rewards_value": "₹3,000",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹250"
        },
        {
          "category": "other_offline_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 3,
      "card_name": "HDFC Shoppers Stop Black Credit Card",
      "bank_name": "HDFC",
      "card_type": "VISA",
      "net_annual_savings": "₹30,690",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹24,000",
      "lounge_value": "₹0",
      "joining_fee": "₹5,310 (incl. GST)",
      "annual_fee": "₹5,310 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 151,
          "brands": [
            {
              "id": 94,
              "name": "Shoppers Stop"
            }
          ],
          "card_id": 158,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "",
          "welcome_benefit_tooltip": "",
          "cash_value": 0
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "all_pharmacy",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "shoppers-stop-black-hdfc-credit-card",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130210_BankKaro_20251121_162054748"
    },
    {
      "rank": 4,
      "card_name": "CRED IndusInd Bank Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "RuPay",
      "net_annual_savings": "₹29,411",
      "annual_rewards_value": "₹30,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "₹589 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹2,500"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "cred-indusind-bank-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260625_173501453_Mockup_45.png"
    },
    {
      "rank": 5,
      "card_name": "IndusInd Tiger Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹26,000",
      "annual_rewards_value": "₹6,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹500"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "indusind-tiger-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125059_BankKaro_Mockup_Desktop_1.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-landmark-reward-select-credit-card"}</summary>

```
{
  "name": "SBI Landmark Reward SELECT Credit Card",
  "nick_name": "SBI Landmark Reward SELECT, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.2,
  "user_ratings": 449,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "Not Applicable",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.50% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currencyExamples (3.5%):₹100 → ₹3.50₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.50% of the withdrawn amount is charged on cash advances using the credit card minimum ₹500, if applicable",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1,000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1,001 - ₹10,000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10,001 - ₹25,000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25,001 - ₹50,000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50,000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "An additional ₹100 applies if the Minimum Amount Due is not paid for two consecutive billing cycles",
    "tnc_url": "https://www.sbicard.com/en/most-important-terms-and-conditions.page"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.25",
    "redemption_options": "• Gift Vouchers\n• Merchandise&nbsp;",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI",
    "exclusion_spends": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 10000,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Earn 15 Reward Points per ₹100 Spent at Online and Retail Landmark Stores",
      "description": "Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy all earn the accelerated rate, with no monthly or annual earning cap"
    },
    {
      "title": "Earn 10 Reward Points per ₹100 Spent on",
      "description": "restaurant bills, movie ticket spends and all international transaction"
    }
  ],
  "tags": [
    "Shopping",
    "Dining"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• earn 15 Reward Points per ₹100 spent at online and retail Landmark Stores Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy\n• 10 Reward Points per ₹100 spent on dining, movies and international spends\n• The milestone benefit gives 12,000 bonus Reward Points on overall annual retail spends of ₹3,00,000\n• Reward Points can also be converted into Landmark Rewards at 2.4 Reward Points = 1 LMR, with 1 LMR = ₹0.60"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Get 6,000 bonus Reward Points worth ₹1,500 on payment of the annual fee"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on movies"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on dining"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver at all petrol pumps across India, on transactions between ₹500 and ₹3,000. Maximum waiver of ₹100 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25001,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "sbi-landmark-reward-select-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

## Q5 run 2 [mixed monthly/annual]
**What to check:** Education/school-fee spends: rewards usually excluded or surcharged. Does the tool/bot say so?

**User:** My total spend is around 50k a month, mostly online shopping, plus 36,000 a year for school fees. Suggest a card.

**Bot:** Based on your spending, the **Ixigo AU Credit Card** saves you **₹35,000 per year**. 

Your spending of **₹50,000/month on online shopping** can earn you significant benefits, and this card has a **joining fee of ₹0**.

### Key Details:
- **Net Annual Savings**: ₹35,000
- **Annual Rewards Value**: ₹15,000
- **Milestone Benefits**: ₹20,000
- **Lounge Access Value**: ₹0 (no complimentary access)

![Ixigo AU Credit Card](https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png)

### Other Options:
1. **SBI Landmark Reward SELECT Credit Card**
   - Net Savings: ₹31,231
   - Annual Fee: ₹1,769 (incl. GST)

2. **HDFC Shoppers Stop Black Credit Card**
   - Net Savings: ₹30,690
   - Annual Fee: ₹5,310 (incl. GST)

3. **CRED IndusInd Bank Credit Card**
   - Net Savings: ₹29,411
   - Annual Fee: ₹589 (incl. GST)

Would you like to compare the top two options further or check your eligibility? Check the bank's current terms before applying; approval is the bank's decision.

Note from the tool data: the net savings figure from the recommendation tool does not subtract the joining fee (SBI Landmark Reward SELECT Credit Card: joining fee ₹1,769 (incl. GST); HDFC Shoppers Stop Black Credit Card: joining fee ₹5,310 (incl. GST)).
Note from the card details tool: CRED IndusInd Bank Credit Card lists 'School & Education Service' under rewards exclusions, so your school_fees spend may earn nothing on this card.

<details><summary>recommend_cards {"other_online_spends": 50000, "school_fees": 3000}</summary>

```
{
  "total_cards_analyzed": 204,
  "recommendations": [
    {
      "rank": 1,
      "card_name": "ixigo AU credot Card",
      "bank_name": "AU Small Finance Bank",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹35,000",
      "annual_rewards_value": "₹15,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 225,
          "brands": [
            {
              "id": 471,
              "name": "Ixigo"
            }
          ],
          "card_id": 239,
          "rp_bonus": "1000",
          "maximum_days": "30",
          "minimum_spend": "100",
          "voucher_bonus": "1000",
          "cash_conversion": "1",
          "welcome_benefit_tooltip": "",
          "cash_value": 2000
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹1,250"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "all_pharmacy",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "ixigo-au-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260729_143058744_AU_ALTURA__2.png"
    },
    {
      "rank": 2,
      "card_name": "SBI Landmark Reward SELECT Credit Card",
      "bank_name": "SBI",
      "card_type": "VISA,RuPay",
      "net_annual_savings": "₹31,231",
      "annual_rewards_value": "₹3,000",
      "milestone_benefits": "₹30,000",
      "lounge_value": "₹0",
      "joining_fee": "₹1,769 (incl. GST)",
      "annual_fee": "₹1,769 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 196,
          "brands": [],
          "card_id": 263,
          "rp_bonus": "6000",
          "maximum_days": "",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "0.25",
          "welcome_benefit_tooltip": "",
          "cash_value": 1500
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹250"
        },
        {
          "category": "other_offline_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flights_annual",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "sbi-landmark-reward-select-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png"
    },
    {
      "rank": 3,
      "card_name": "HDFC Shoppers Stop Black Credit Card",
      "bank_name": "HDFC",
      "card_type": "VISA",
      "net_annual_savings": "₹30,690",
      "annual_rewards_value": "₹12,000",
      "milestone_benefits": "₹24,000",
      "lounge_value": "₹0",
      "joining_fee": "₹5,310 (incl. GST)",
      "annual_fee": "₹5,310 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [
        {
          "id": 151,
          "brands": [
            {
              "id": 94,
              "name": "Shoppers Stop"
            }
          ],
          "card_id": 158,
          "rp_bonus": "",
          "maximum_days": "30",
          "minimum_spend": "",
          "voucher_bonus": "",
          "cash_conversion": "",
          "welcome_benefit_tooltip": "",
          "cash_value": 0
        }
      ],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹1,000"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "all_pharmacy",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "shoppers-stop-black-hdfc-credit-card",
      "rating": 4.1,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130210_BankKaro_20251121_162054748"
    },
    {
      "rank": 4,
      "card_name": "CRED IndusInd Bank Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "RuPay",
      "net_annual_savings": "₹29,411",
      "annual_rewards_value": "₹30,000",
      "milestone_benefits": "₹0",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "₹589 (incl. GST)",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹2,500"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "flipkart_spends",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "cred-indusind-bank-credit-card",
      "rating": 4.2,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260625_173501453_Mockup_45.png"
    },
    {
      "rank": 5,
      "card_name": "IndusInd Tiger Credit Card",
      "bank_name": "IndusInd Bank",
      "card_type": "VISA",
      "net_annual_savings": "₹26,000",
      "annual_rewards_value": "₹6,000",
      "milestone_benefits": "₹20,000",
      "lounge_value": "₹0",
      "joining_fee": "Free",
      "annual_fee": "Free",
      "annual_fee_waived": false,
      "welcome_benefits": [],
      "voucher": null,
      "lounge_access": {
        "domestic_per_quarter": 0,
        "international_per_quarter": 0,
        "domestic_value_used": "₹0",
        "international_value_used": "₹0"
      },
      "top_spend_categories": [
        {
          "category": "other_online_spends",
          "annual_value": "₹500"
        },
        {
          "category": "amazon_spends",
          "annual_value": "₹0"
        },
        {
          "category": "dining_or_going_out",
          "annual_value": "₹0"
        }
      ],
      "card_alias": "indusind-tiger-credit-card",
      "rating": 4,
      "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_125059_BankKaro_Mockup_Desktop_1.png"
    }
  ],
  "_format_hint": "net_annual_savings = annual_rewards + milestone_benefits + lounge_value - annual_fee. Lead with this. top_spend_categories shows where savings come from."
}
```
</details>

<details><summary>get_card_details {"card_alias": "sbi-landmark-reward-select-credit-card"}</summary>

```
{
  "name": "SBI Landmark Reward SELECT Credit Card",
  "nick_name": "SBI Landmark Reward SELECT, Credit Card",
  "bank": "SBI",
  "bank_id": 3,
  "card_type": "VISA,RuPay",
  "card_network": null,
  "rating": 4.2,
  "user_ratings": 449,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260818_105810829_Mockup_64.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹1,769 (₹1,499 + GST)",
    "joining_note": null,
    "annual": "₹1,769 (₹1,499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "Not Applicable",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.50% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currencyExamples (3.5%):₹100 → ₹3.50₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.50% of the withdrawn amount is charged on cash advances using the credit card minimum ₹500, if applicable",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "₹199",
    "cash_payment_fee": "₹250",
    "cheque_payment_fee": "₹200",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 - ₹500",
        "fee": "₹0"
      },
      {
        "outstanding": "₹501 - ₹1,000",
        "fee": "₹400"
      },
      {
        "outstanding": "₹1,001 - ₹10,000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10,001 - ₹25,000",
        "fee": "₹950"
      },
      {
        "outstanding": "₹25,001 - ₹50,000",
        "fee": "₹1100"
      },
      {
        "outstanding": "Above ₹50,000",
        "fee": "₹1300"
      }
    ],
    "late_payment_note": "An additional ₹100 applies if the Minimum Amount Due is not paid for two consecutive billing cycles",
    "tnc_url": "https://www.sbicard.com/en/most-important-terms-and-conditions.page"
  },
  "rewards": {
    "point_value": "1 Reward Point = ₹0.25",
    "redemption_options": "• Gift Vouchers\n• Merchandise&nbsp;",
    "redemption_catalogue": "https://www.sbicard.com/en/personal/rewards.page",
    "exclusions": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI",
    "exclusion_spends": "Fuel, Rent, Government Spends, Gaming, Wallet, EMI"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 10000,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Earn 15 Reward Points per ₹100 Spent at Online and Retail Landmark Stores",
      "description": "Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy all earn the accelerated rate, with no monthly or annual earning cap"
    },
    {
      "title": "Earn 10 Reward Points per ₹100 Spent on",
      "description": "restaurant bills, movie ticket spends and all international transaction"
    }
  ],
  "tags": [
    "Shopping",
    "Dining"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• earn 15 Reward Points per ₹100 spent at online and retail Landmark Stores Lifestyle, Home Centre, Max, Spar, Babyshop and EasyBuy\n• 10 Reward Points per ₹100 spent on dining, movies and international spends\n• The milestone benefit gives 12,000 bonus Reward Points on overall annual retail spends of ₹3,00,000\n• Reward Points can also be converted into Landmark Rewards at 2.4 Reward Points = 1 LMR, with 1 LMR = ₹0.60"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Get 6,000 bonus Reward Points worth ₹1,500 on payment of the annual fee"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on movies"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• Enjoy 10 Reward Points per ₹100 spent on dining"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver at all petrol pumps across India, on transactions between ₹500 and ₹3,000. Maximum waiver of ₹100 per statement cycle"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25001,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "sbi-landmark-reward-select-credit-card"
}
```
</details>

<details><summary>get_card_details {"card_alias": "shoppers-stop-black-hdfc-credit-card"}</summary>

```
{
  "name": "HDFC Shoppers Stop Black Credit Card",
  "nick_name": "Shoppers Stop Black",
  "bank": "HDFC",
  "bank_id": 6,
  "card_type": "VISA",
  "card_network": null,
  "rating": 4.1,
  "user_ratings": 461,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260622_130210_BankKaro_20251121_162054748",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "₹5,310 (₹4,500 + GST)",
    "joining_note": "A one-time joining fee of ₹4,500 plus applicable taxes is charged at the time of card issuance as per the bank's policy.",
    "annual": "₹5,310 (₹4,500 + GST)",
    "annual_note": "Not Applicable",
    "annual_fee_waiver": "The annual fee is not waived under any spending conditions.",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.75%",
    "apr_annual": "45.00%",
    "forex_markup": "3.50%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currency.Examples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.50%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card (minimum ₹500, if applicable).",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "1% railway ticket purchase fee applies.",
    "rent_payment_fee": "1%",
    "cash_payment_fee": "₹100",
    "cheque_payment_fee": "₹100",
    "reward_redemption_fee": "₹99",
    "late_payment_slabs": [
      {
        "outstanding": "₹0 – ₹100",
        "fee": "₹0"
      },
      {
        "outstanding": "₹101 – ₹500",
        "fee": "₹100"
      },
      {
        "outstanding": "₹501 – ₹1,000",
        "fee": "₹500"
      },
      {
        "outstanding": "₹1,001 – ₹5,000",
        "fee": "₹600"
      },
      {
        "outstanding": "₹5,001 – ₹10,000",
        "fee": "₹750"
      },
      {
        "outstanding": "₹10,001 – ₹25,000",
        "fee": "₹900"
      },
      {
        "outstanding": "₹25,001 – ₹50,000",
        "fee": "₹1,100"
      },
      {
        "outstanding": "₹50,000+",
        "fee": "₹1,300"
      }
    ],
    "late_payment_note": "Late payment charges on the HDFC Shoppers Stop Black Credit Card depend on the total outstanding balance. No fee is charged for balances up to ₹100. A nominal fee is charged for balances between ₹101 and ₹500. As the outstanding amount increases, the late fee progressively rises, with moderate fees for mid-range balances and higher fees for large outstanding dues, going up to a maximum penalty for balances exceeding ₹50,000.",
    "tnc_url": "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/personal-banking/discover-products/cards/credit-cards/personal-mitc/mitc-in-english.pdf"
  },
  "rewards": {
    "point_value": "1 reward point = ₹1",
    "redemption_options": "• Shoppers Stop vouchers\n• Airmiles/Travel Bookings (via SmartBuy)\n• Cashback\n• Product Catalogue",
    "redemption_catalogue": "https://offers.smartbuy.hdfc.bank.in/v2/foryou",
    "exclusions": "Fuel, Insurance, DCC (Dynamic Currency Conversion) transactions, International transactions",
    "exclusion_spends": "Fuel, Insurance, DCC (Dynamic Currency Conversion), Gold and Jewelry, Cash Withdrawals, EMI, Balance Transfer"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 200000,
  "milestone_benefits": [
    {
      "spend_target": null,
      "reward": null,
      "description": null
    }
  ],
  "key_benefits": [
    {
      "title": "Earn 7% Reward Points on Shoppers Stop",
      "description": "Spends on all online and offline purchases at Shoppers Stop, capped at 2,000 reward points per month"
    },
    {
      "title": "Enjoy 16 Domestic and 8 International Lounge",
      "description": "Visits per year (maximum 4 domestic and 2 international per quarter), along with accidental air death cover of ₹3 crore and emergency overseas hospitalization cover up to ₹50 lakh"
    },
    {
      "title": "Get Complimentary Shoppers Stop Black Membership",
      "description": "worth ₹4,500 on card issuance, with exclusive discounts, offers and First Citizen Black tier privileges"
    },
    {
      "title": "Earn 2% Reward Points",
      "description": "on all other Non - Shoppers Stop spends, capped at 2,000 points per month"
    },
    {
      "title": "Earn ₹1,500 Benefit for ₹50,000 Purchase",
      "description": "at Shoppers Stop on weekends (capped 5 times per year)"
    },
    {
      "title": "Earn ₹2,000 on Weekend Spends of ₹50,000",
      "description": "at Shoppers Stop on weekends, once per month, capped at 5 times per year"
    }
  ],
  "tags": [
    "Shopping",
    "Travel"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• 20 First Citizen points per ₹200 spent on private label brands at Shoppers Stop (unlimited)\n• 12 First Citizen points per ₹200 spent on beauty products and other brands at Shoppers Stop (unlimited)\n• 2 First Citizen points per ₹200 spent on all other eligible spends (unlimited)1% fuel surcharge waiver on fuel transactions between ₹400 and ₹5,000, capped at ₹400 per statement month.\n• 15% instant discount on EazyDiner on orders above ₹2,500, up&nbsp;&nbsp;"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• Complimentary Shoppers Stop vouchers worth ₹2,250 redeemable at Shoppers Stop and HomeStop on card issuance\n• 300 First Citizen reward points (worth ₹300) on first transaction within 30 days of card issuance\n• Complimentary First Citizen Club Golden Glow Membership on card issuance, with benefits including 45-day extended exchange period, free home delivery and birthday offers"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• Enjoy 16 Domestic and 8 International Lounge visits per year, maximum 4 domestic and 2 International per quarter&nbsp;"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• 15% instant discount on EazyDiner on orders above ₹2,500, up to ₹500 per month"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver on all fuel transactions between ₹400 and ₹5,000, capped at ₹400 per statement month"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offers",
      "details": "• Exclusive access to 2 end-of-season sales and 1 festive sale per year at Shoppers Stop.&lt;/li&gt;&lt;li&gt;Free home delivery on in-store and online purchases made using the card"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 8.4,
    "income_self_emp_lpa": 8.4,
    "min_income_monthly": 70000,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "shoppers-stop-black-hdfc-credit-card"
}
```
</details>

<details><summary>get_card_details {"card_alias": "cred-indusind-bank-credit-card"}</summary>

```
{
  "name": "CRED IndusInd Bank Credit Card",
  "nick_name": "CRED IndusInd, Credit Card",
  "bank": "IndusInd Bank",
  "bank_id": 8,
  "card_type": "RuPay",
  "card_network": null,
  "rating": 4.2,
  "user_ratings": 486,
  "image": "https://d2sriifpjiqv0p.cloudfront.net/admin/BankKaro_20260625_173501453_Mockup_45.png",
  "priority_tag": null,
  "invite_only": false,
  "employment_type": "both",
  "new_to_credit": true,
  "existing_customer_only": false,
  "fees": {
    "joining": "Free",
    "joining_note": null,
    "annual": "₹589 (₹499 + GST)",
    "annual_note": null,
    "annual_fee_waiver": "Not Applicable",
    "gst_note": "All fees include 18% GST."
  },
  "fee_schedule": {
    "apr_monthly": "3.95%",
    "apr_annual": "47.40%",
    "forex_markup": "3.5%",
    "forex_markup_note": "3.5% forex markup is charged on transactions made in currencies other than INR. Applies to international POS payments and online purchases charged in foreign currencyExamples (3.5%):₹100 → ₹3.5₹1,000 → ₹35₹10,000 → ₹350₹1,00,000 → ₹3,500",
    "atm_withdrawal_fee": "2.5%",
    "atm_withdrawal_note": "2.5% of the withdrawn amount is charged on cash advances using the credit card, minimum ₹300, if applicable",
    "railway_surcharge": "1%",
    "railway_surcharge_note": "A surcharge of 1% is applied to transactions made for booking railway tickets",
    "rent_payment_fee": "1%",
    "cash_payment_fee": "₹100",
    "cheque_payment_fee": "₹250",
    "reward_redemption_fee": "Not Applicable",
    "late_payment_slabs": [
      {
        "outstanding": "₹0–₹100",
        "fee": "₹0"
      },
      {
        "outstanding": "₹101–₹500",
        "fee": "₹100"
      },
      {
        "outstanding": "₹501–₹1,000",
        "fee": "₹350"
      },
      {
        "outstanding": "₹1,001–₹10,000",
        "fee": "₹550"
      },
      {
        "outstanding": "₹10,001–₹25,000",
        "fee": "₹800"
      },
      {
        "outstanding": "₹25,001–₹50,000",
        "fee": "₹1,100"
      },
      {
        "outstanding": "Above ₹50,000",
        "fee": "₹1,300"
      }
    ],
    "late_payment_note": "Additional ₹100 is charged if Minimum Amount Due remains unpaid for two consecutive cycles, continuing until cleared",
    "tnc_url": "https://www.indusind.bank.in/content/dam/indusind-corporate/credit-cards/MITC_Premium.pdf"
  },
  "rewards": {
    "point_value": "1 Cred Point = ₹1",
    "redemption_options": "• Flight &amp; Hotel Booking\n• CRED Store Purchases",
    "redemption_catalogue": "https://cred.club/",
    "exclusions": "School & Education Service, Government Institutions, Wallet Load, Rent, Jewellery, Fuel, Quasi Cash, Cash Withdrawal",
    "exclusion_spends": "School & Education Service, Government Institutions, Wallet Load, Rent, Jewellery, Fuel, Quasi Cash, Cash Withdrawal"
  },
  "welcome_benefits": null,
  "lounge_summary": null,
  "annual_saving_claimed": 10000,
  "milestone_benefits": null,
  "key_benefits": [
    {
      "title": "Earn 5% back as CRED Points on all E-commerce Transactions",
      "description": "made with the card accelerated earn capped at 5,000 CRED Points per statement cycle"
    },
    {
      "title": "Earn 5% back as CRED Points on CRED UPI",
      "description": "Payments, earn rewards on everyday UPI spends"
    },
    {
      "title": "Earn 1% Back as CRED Points on Utility and Insurance Bill",
      "description": "payments made via the CRED app"
    }
  ],
  "tags": [
    "Shopping",
    "Utility Bills",
    "UPI"
  ],
  "detailed_benefits": [
    {
      "type": "all",
      "sub_type": "All Benefits",
      "details": "• Co-Branded RuPay rewards card earning CRED Points on every spend 5% back on E-commerce\n• CRED app and CRED UPI transactions capped at 5,000 CRED Points cycle\n• 1% back on Scan &amp; Pay, Utility &amp; Insurance bills, all other spends and international transactions\n• The card is enabled on UPI &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;"
    },
    {
      "type": "welcome",
      "sub_type": "Welcome Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Flight Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Railway Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Cab Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "travel",
      "sub_type": "Bus Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Airport Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "lounge",
      "sub_type": "Railway Lounge Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "movie_ticket",
      "sub_type": "Movie Ticket Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "dining",
      "sub_type": "Dining Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Benefits",
      "details": "• This card does not offer any benefits in this category"
    },
    {
      "type": "fuel",
      "sub_type": "Fuel Surcharge Waiver Benefits",
      "details": "• 1% fuel surcharge waiver across all fuel stations in India, applicable on fuel transactions between ₹500 and ₹5,000"
    },
    {
      "type": "insurance",
      "sub_type": "Insurance Benefits",
      "details": "• Complimentary insurance cover up to an amount equal to the credit limit on the card also available on add-on cards\n• It covers unauthorised transactions in case of loss/theft of card cover up to 48 hours prior to reporting the loss and counterfeit-card fraud"
    },
    {
      "type": "bank_offers",
      "sub_type": "Bank Offer",
      "details": "• This card does not offer any benefits in this category"
    }
  ],
  "eligibility": {
    "min_age": 21,
    "max_age": 60,
    "income_salaried_lpa": 3,
    "income_self_emp_lpa": 3,
    "min_income_monthly": 25000,
    "crif_salaried": 720,
    "crif_self_emp": 720
  },
  "card_alias": "cred-indusind-bank-credit-card"
}
```
</details>

**Verdict (fill in):** OK / WRONG / MADE-UP / MISSING / MISLEADING → cause: model / MCP / data

---

