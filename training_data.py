import datetime

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_day = current_time.weekday()  # Monday is 0, Sunday is 6

if current_day >= 5:  # Weekend check (Saturday or Sunday)
    if current_hour < 12:
        greeting = 'Happy Weekend Morning'
    elif current_hour >= 12 and current_hour < 18:
        greeting = 'Happy Weekend Afternoon'
    else:
        greeting = 'Happy Weekend Evening'
else:  # Weekday greeting
    if current_hour < 12:
        greeting = 'Good Morning'
    elif current_hour >= 12 and current_hour < 18:
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'

training_data = [
    # Greetings
    ("Hello", f"{greeting}! Welcome to Gym Buddy! How can I assist you today?"),
    ("Hi", f"{greeting}! Ready to hit the gym? How can I help you?"),
    ("Good morning", "Good morning! Let's make today a great workout day!"),
    ("Good afternoon", "Good afternoon! How can I support your fitness journey today?"),
    ("Good evening", "Good evening! Ready to unwind with a good workout?"),
    
    # Getting Started
    ("Do I need to be a member to use the gym?", "Yes, our gym operates on a membership basis. We offer various membership options to suit your needs and budget."),
    ("How do I become a member?", "There are three ways to sign up for a membership: Visit our front desk and speak with a friendly staff member. Sign up online through our website. Call us at 079556432 to discuss membership options."),
    ("What if I'm new to exercise?", "We welcome people of all fitness levels! We offer introductory classes and personal training sessions to help you get started on the right foot."),
    ("Do I need to bring my own workout clothes and towels?", "Yes, please bring comfortable workout clothing and a water bottle. Towels are available for purchase at the front desk."),
    ("What are your gym hours?", "Our gym is open for 24 hours, every day. Please check your membership category to know what times you’ll have access."),
    
    # Nutrition Advice
    ("What should I eat before a workout?", "It's best to have a balanced meal with carbohydrates and protein 1-2 hours before your workout. Options include a banana with peanut butter or oatmeal with berries."),
    ("What should I eat after a workout?", "After your workout, focus on protein to aid muscle recovery. Consider options like a protein shake, Greek yogurt, or grilled chicken with vegetables."),
    ("How can I stay hydrated?", "Drink water throughout the day, especially before, during, and after your workout. Aim for at least 8 glasses a day, more if you're exercising vigorously."),
    ("Do you have any healthy snack recommendations?", "Absolutely! Try nuts, fruits, yogurt, or protein bars for quick and healthy snacks."),
    
    # Calendars for Routines
    ("Can you help me create a workout routine?", "Of course! Let’s design a routine. What are your fitness goals: weight loss, muscle gain, or general fitness?"),
    ("What does a weekly workout routine look like?", "A typical weekly routine could include: Monday - Upper body strength, Tuesday - Cardio, Wednesday - Lower body strength, Thursday - Rest, Friday - Full-body workout, Saturday - Active recovery (like yoga), Sunday - Rest."),
    ("What about a daily routine?", "A daily routine might include: Warm-up (5-10 min), Strength training (30-40 min), Cardio (20-30 min), Cool down (5-10 min), Stretching (5-10 min)."),
    ("How can I track my progress?", "Consider using a fitness app or journal to log your workouts and nutrition. Regularly check your progress against your goals."),
    
    # Membership Options
    ("What types of memberships do you offer?", "We offer a variety of membership options to fit your needs and budget. These include: Individual memberships, Couples memberships, Family memberships, Student discounts, Senior citizen discounts, Pay-as-you-go options."),
    ("Can I switch my membership type?", "Yes, you can upgrade or downgrade your membership at any time by contacting our front desk staff."),
    ("What are the payment terms for memberships?", "Most memberships require a monthly commitment with automatic payments. However, we also offer annual memberships at a discounted rate."),
    ("Is there a contract involved with a membership?", "Some memberships require a minimum commitment period, typically one month or one year. Please refer to the specific membership details for more information."),
    ("What happens if I need to cancel my membership?", "We understand that life happens! You can cancel your membership by giving us [Notice Period] written notice. Please refer to your membership agreement for details on cancellation fees."),
    
    # Gym Facilities and Services
    ("What are your peak and off-peak hours?", "Generally, our peak hours are: Weekdays: Early mornings (before 8am) and evenings (after 4pm), Weekends: Mornings (between 9am and 12pm)."),
    ("Do my membership discounts apply during peak hours?", "Some membership discounts, such as student discounts, may not apply during peak hours. Please refer to your specific membership agreement for details."),
    ("Is the gym less crowded during off-peak hours?", "Yes, the gym is typically less crowded during off-peak hours. This can be a good option if you prefer a quieter workout environment."),
    ("What kind of equipment do you have?", "Our gym boasts a wide variety of state-of-the-art equipment, including: Cardio machines (treadmills, ellipticals, stationary bikes), Strength training machines (weight benches, free weights, cable machines), Functional training equipment (medicine balls, TRX trainers, kettlebells), Group fitness studios for classes."),
    ("Do you offer locker rooms with showers?", "Yes, we have clean and well-maintained locker rooms with showers, toilets, and changing areas. Get your padlocks for the lockers."),
    ("Do you have Wi-Fi available?", "Yes, we offer free Wi-Fi access for our members."),
    ("Is there a juice bar or cafe on-site?", "We do not have a full-service cafe, but we offer a selection of healthy snacks and beverages for purchase. There is water at the water fountain, free for everyone."),
    ("Do you provide childcare services?", "Unfortunately, we do not offer on-site childcare services at this time."),
    
    # Personal Training
    ("Do you offer personal training services?", "Absolutely! We have a team of certified and experienced personal trainers who can create a personalized workout program to help you reach your fitness goals."),
    ("How much does personal training cost?", "The cost of personal training varies depending on the trainer's experience, the number of sessions purchased, and the package chosen. We offer consultations to discuss your needs and provide a personalized quote."),
    ("What if I'm new to exercise and need some guidance?", "Personal training is a great option for beginners! Your trainer will design a safe and effective program tailored to your fitness level and goals."),
    ("Can I train with a friend or group?", "Yes, we offer small group personal training sessions, which can be a cost-effective and motivating way to train with friends."),
    ("How do I schedule a personal training consultation?", "Contact our front desk staff or visit our website to book a consultation with a personal trainer."),
    
    # Policies
    ("What is your guest policy?", "Members are welcome to bring a guest for a day fee. Guests must complete a waiver form before using the gym facilities."),
    ("What is your dress code?", "We require proper workout attire that is clean and modest. Please refrain from wearing denim, street shoes, or revealing clothing."),
    ("Do you have a lost and found?", "Yes, we have a lost and found for any items left behind in the gym. Unclaimed items are donated to charity after a certain period."),
    ("What is your policy on food and drinks in the gym?", "We ask that members refrain from bringing outside food or drinks into the gym. We offer a selection of healthy snacks and beverages for purchase."),
    ("Do you allow pets in the gym?", "Unfortunately, no pets are allowed in the gym for safety and hygiene reasons. Service animals are permitted."),
    
    # Safety
    ("Do you have staff on-site to assist with workouts?", "Yes, we have certified fitness professionals available on the gym floor to answer questions and provide guidance."),
    ("What kind of safety equipment do you have?", "We provide first-aid kits and automated external defibrillators (AEDs) on-site in case of emergencies."),
    ("Do you require members to undergo a fitness assessment?", "While not mandatory, we recommend a fitness assessment for new members, especially those with pre-existing health conditions. This helps us personalize your workout program and ensure your safety."),
    ("What should I do if I get injured while working out?", "Inform a staff member immediately if you experience any pain or injury while using the gym facilities."),
    ("Do you offer CPR or first-aid training?", "We may offer occasional CPR or first-aid training courses. Please inquire at the front desk for details."),
    
    # Community
    ("How can I get involved in the gym community?", "We offer a variety of group fitness classes, workshops, and social events throughout the month. These are great opportunities to meet other members, stay motivated, and learn something new."),
    ("If I have further questions, how can I contact you?", "If you have any further questions, please don't hesitate to contact our friendly staff at 012345 or email us at info@gymbuddy.com."),
]

