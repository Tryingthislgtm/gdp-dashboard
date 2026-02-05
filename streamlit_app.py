import streamlit as st
from datetime import datetime, timedelta
from pricing_plans_loader import get_pricing_plans

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Promotion Calculator',
    page_icon=':camera:',
    layout='wide',
)

# Load pricing plans
plans_df = get_pricing_plans()
plan_names = plans_df['PlanName'].tolist()

# Title
'''
# :camera: Promotion Calculator for Customers

Calculate the impact of promotions and plan switches on customer bills in real-time.
Help your team communicate pricing and savings clearly to customers.
'''

''

# Create three columns for input and results
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader('📋 Current Plan')
    
    # Customer current plan selection
    current_plan = st.selectbox(
        'Customer\'s Current Plan',
        plan_names,
        index=1  # Default to Professional Standard
    )
    
    current_plan_data = plans_df[plans_df['PlanName'] == current_plan].iloc[0]
    current_plan_price = current_plan_data['BasePrice']
    
    # Number of lenses for this customer (affects pricing totals)
    num_lenses = st.number_input(
        'Number of Lenses',
        min_value=1,
        max_value=200,
        value=1,
        step=1,
    )

    current_plan_price_total = current_plan_price * int(num_lenses)

    st.info(
        f"**Current:** {current_plan}\n\n{current_plan_data['Description']}\n\n💰 ${current_plan_price:,.2f}/lens — ${current_plan_price_total:,.2f}/month total"
    )
    
    ''
    
    st.subheader('🔄 Switch to Plan')
    
    # Available plans to switch to (excluding current plan)
    available_plans = [p for p in plan_names if p != current_plan]
    
    switch_plan = st.selectbox(
        'Available Plans to Switch To',
        available_plans,
        key='switch_plan_selector'
    )
    
    switch_plan_data = plans_df[plans_df['PlanName'] == switch_plan].iloc[0]
    switch_plan_price = switch_plan_data['BasePrice']
    switch_plan_price_total = switch_plan_price * int(num_lenses)
    plan_switch_savings = current_plan_price_total - switch_plan_price_total

    st.info(
        f"**New Plan:** {switch_plan}\n\n{switch_plan_data['Description']}\n\n💰 ${switch_plan_price:,.2f}/lens — ${switch_plan_price_total:,.2f}/month total"
    )
    
    if plan_switch_savings > 0:
        st.success(f'💡 **Switch savings: ${plan_switch_savings:,.2f}/month** from plan change alone!')
    elif plan_switch_savings < 0:
        st.warning(f'⚠️ This plan costs ${abs(plan_switch_savings):,.2f} more per month')
    else:
        st.info('Same price - different features!')
    
    ''
    
    st.subheader('🎯 Additional Promotion')
    
    # Promotion type selection
    promo_type = st.radio(
        'Promotion Type',
        ['Percentage Discount', 'Flat Amount Discount', 'No Additional Promo'],
        horizontal=True
    )
    
    if promo_type == 'Percentage Discount':
        promo_value = st.slider(
            'Discount Percentage (%)',
            min_value=0,
            max_value=100,
            value=10,
            step=1
        )
        # Discount applies to the total switched plan price (all lenses)
        discount_amount = switch_plan_price_total * (promo_value / 100)
    elif promo_type == 'Flat Amount Discount':
        promo_value = st.number_input(
            'Flat Discount Amount ($)',
            min_value=0.0,
            value=20.0,
            step=5.0,
            format='%.2f'
        )
        # Flat discount applied against the total switched plan price
        discount_amount = min(promo_value, switch_plan_price_total)
    else:
        discount_amount = 0.0
    
    ''
    
    # Optional promotion code
    promo_code = st.text_input(
        'Promotion Code (optional)',
        placeholder='e.g., SWITCH2026'
    )
    
    ''
    
    st.subheader('📅 Billing Period')
    
    # Bill start date
    bill_start_date = st.date_input(
        'Plan Switch Effective Date',
        value=datetime.today(),
    )

with col2:
    st.subheader('📊 Billing Comparison')
    
    # Use the switched plan price as base for calculations (total for all lenses)
    base_price = switch_plan_price_total
    
    # Calculate final bill with taxes and fees
    bill_after_discount = base_price - discount_amount
    
    # Tax calculation (example: 8.5%)
    tax_rate = 0.085
    taxes = bill_after_discount * tax_rate
    
    # Processing fee (example: 2.5% or $15, whichever is higher)
    processing_fee = max(15.0, bill_after_discount * 0.025)
    
    final_bill = bill_after_discount + taxes + processing_fee
    
    # Total savings (plan switch + promotion)
    total_savings = plan_switch_savings + discount_amount
    savings_percent = (total_savings / current_plan_price_total * 100) if current_plan_price_total > 0 else 0
    
    # Display metrics
    metric_cols = st.columns(3)
    
    with metric_cols[0]:
        st.metric(
            label='Current Plan',
            value=f'${current_plan_price_total:,.2f}',
            delta=None,
        )
    
    with metric_cols[1]:
        st.metric(
            label='Total Savings',
            value=f'${total_savings:,.2f}',
            delta=f'{savings_percent:.1f}%',
            delta_color='normal',
        )
    
    with metric_cols[2]:
        st.metric(
            label='New Monthly Bill',
            value=f'${final_bill:,.2f}',
            delta='All fees included',
            delta_color='off',
        )
    
    ''
    ''
    
    # Breakdown table
    st.subheader('Detailed Monthly Breakdown')
    
    breakdown_data = {
        'Item': [
            f'Current Plan ({current_plan})',
            'Plan Switch Savings',
            f'New Plan ({switch_plan})',
            'Additional Promotion Discount',
            'Subtotal After Discounts',
            'Taxes (8.5%)',
            'Processing Fee',
            'FINAL MONTHLY BILL'
        ],
        'Amount': [
            f'${current_plan_price_total:,.2f}',
            f'-${plan_switch_savings:,.2f}',
            f'${switch_plan_price_total:,.2f}',
            f'-${discount_amount:,.2f}',
            f'${bill_after_discount:,.2f}',
            f'${taxes:,.2f}',
            f'${processing_fee:,.2f}',
            f'${final_bill:,.2f}'
        ]
    }
    
    st.table(breakdown_data)
    
    ''
    
    # Promo code display
    if promo_code:
        st.info(f'✅ Promotion Code Applied: **{promo_code.upper()}**')
    
    ''
    
    # Call to action
    st.success(
        f'💡 **Customer saves ${total_savings:,.2f}/month** with plan switch {f"+ promotion!" if discount_amount > 0 else "!"}**\n\n'
        f'Effective: {bill_start_date.strftime("%B %d, %Y")}'
    )

''
''
''

# Communications section
st.header('📞 How to Communicate This to Your Customer', divider='blue')

''

# Create tabs for different communication methods
tab1, tab2, tab3 = st.tabs(['📱 SMS Message', '📧 Email Template', '📋 Phone Script'])

with tab1:
    st.subheader('Text Message for Quick Confirmation')
    
    sms_message = f'''Hi [Customer Name]! 🎉

Great news! We found a better plan for you:

Current Plan: {current_plan} (${current_plan_price:,.2f}/mo)
Better Plan: {switch_plan} (${switch_plan_price:,.2f}/mo)
{f'+ Promotion: {discount_amount:,.2f} off!' if discount_amount > 0 else ''}

Your NEW bill: ${final_bill:,.2f}/mo
Monthly Savings: ${total_savings:,.2f} ({savings_percent:.0f}%)

Effective: {bill_start_date.strftime('%b %d, %Y')}

{f"Code: {promo_code.upper()}" if promo_code else ""}

Ready? Reply YES or call us!'''
    
    # Show totals (all lenses) in the message
    sms_message = sms_message.replace(f"(${current_plan_price:,.2f}/mo)", f"(${current_plan_price_total:,.2f}/mo)")
    sms_message = sms_message.replace(f"(${switch_plan_price:,.2f}/mo)", f"(${switch_plan_price_total:,.2f}/mo)")
    st.code(sms_message, language='plaintext')
    
    st.info(f'📊 **Message Length:** {len(sms_message)} characters ({(len(sms_message) // 160) + 1} SMS)')

with tab2:
    st.subheader('Professional Email Template')
    
    email_subject = f"Switch Plans & Save ${total_savings:,.2f}/Month"
    
    email_body = f'''Dear [Customer Name],

We've reviewed your account and found you could save significant money by switching to a better plan for your needs!

---

CURRENT SITUATION:
Plan: {current_plan}
Monthly Cost: ${current_plan_price_total:,.2f}

RECOMMENDED SWITCH:
Plan: {switch_plan}
Monthly Cost: ${switch_plan_price_total:,.2f}

Plan Switch Savings: -${plan_switch_savings:,.2f}/month
{f'Special Promotional Discount: -${discount_amount:,.2f}/month' if discount_amount > 0 else ''}
────────────────────────────────
TOTAL MONTHLY SAVINGS: ${total_savings:,.2f} ({savings_percent:.1f}%)

---

YOUR NEW BILL:

New Plan Base Price:            ${switch_plan_price_total:,.2f}
{f'Promotional Discount:          -${discount_amount:,.2f}' if discount_amount > 0 else ''}
Subtotal:                       ${bill_after_discount:,.2f}
Taxes (8.5%):                  ${taxes:,.2f}
Processing Fee:                 ${processing_fee:,.2f}
────────────────────────────────
NEW MONTHLY BILL:               ${final_bill:,.2f}

ANNUAL SAVINGS: ${total_savings * 12:,.2f}

EFFECTIVE DATE: {bill_start_date.strftime('%B %d, %Y')}

{f"PROMOTION CODE: {promo_code.upper()}" if promo_code else ""}

---

PLAN FEATURES:

Current Plan ({current_plan}):
{current_plan_data['Features']}

New Plan ({switch_plan}):
{switch_plan_data['Features']}

---

If you'd like to accept this switch, simply reply to this email or call us at 1-800-XXX-XXXX.

Thank you for your business!

Best regards,
[Your Name]
[Your Title]
[Company Name]'''
    
    st.code(email_body, language='plaintext')
    
    # Show email subject
    st.info(f'**Subject Line:** {email_subject}')

with tab3:
    st.subheader('Phone Script for Team')
    
    phone_script = f'''
"Hi [Customer Name], thanks for being a customer! I'm calling because I found a way to save you money.

I've been reviewing your account, and I think you might be overpaying for the plan you're currently on.

Right now you're on our {current_plan} plan at ${current_plan_price_total:,.2f} per month.

Based on your usage, I'd recommend switching to our {switch_plan} plan. It's actually got better features AND it's cheaper:

📊 CURRENT PLAN:
  Plan: {current_plan}
    Cost: ${current_plan_price_total:,.2f}/month

📊 RECOMMENDED PLAN:
  Plan: {switch_plan}
    Cost: ${switch_plan_price_total:,.2f}/month
  
  ✅ Savings from the plan switch: ${plan_switch_savings:,.2f}/month

{f"And here's the best part — we also have a special promotion right now that'll save you an additional ${discount_amount:,.2f}/month." if discount_amount > 0 else ""}

{f"So your total monthly savings would be: ${total_savings:,.2f}/month" if discount_amount > 0 else f"So your new monthly bill would be: ${switch_plan_price_total:,.2f}/month"}

That's ${total_savings * 12:,.2f} in annual savings.

Your new bill would be ${final_bill:,.2f}/month, which includes everything — taxes, fees, everything.

This would be effective {bill_start_date.strftime('%B %d, %Y')}.

{f'And I can give you promotion code {promo_code.upper()} to make sure you get that discount.' if promo_code else ''}

What do you think? Would you like to make that switch?"
'''
    
    st.code(phone_script, language='plaintext')
    
    # Key talking points
    st.info('''
    **Key Points to Emphasize:**
    ✅ Current plan vs. new plan comparison
    ✅ Monthly savings amount
    ✅ Annual savings (multiply by 12)
    ✅ That it has BETTER features (not just cheaper)
    ✅ Additional promotion on top
    ✅ Effective date
    ✅ Promotion code for documentation
    ''')

''
''
''

# Footer with instructions
with st.expander('📋 How to use this calculator'):
    st.markdown('''
    ## For Your Sales Team:
    
    ### Step-by-Step:
    1. **Select Customer's Current Plan** — Choose the plan they're on now
    2. **Choose Plan to Switch To** — Pick a better or cheaper plan for them
    3. **Add Any Additional Promotion** — Apply percentage or flat discount on top
    4. **Add Promo Code** — For tracking and documentation
    5. **Set Effective Date** — When the switch takes effect
    6. **Use Communication Templates** — Copy SMS, Email, or Phone Script
    
    ## Real-World Workflow:
    
    - **Scenario 1:** Customer on expensive plan → Switch them to cheaper plan with same features
    - **Scenario 2:** Customer on basic plan → Upsell to professional with promotion discount
    - **Scenario 3:** Customer churning → Offer plan switch + special discount
    
    ## Why This Works:
    - Shows TOTAL savings (plan + promo combined)
    - Proves new plan has better features
    - Builds confidence with clear breakdown
    - Annual savings number seals the deal
    - Multiple communication channels = higher acceptance
    
    ## Pro Tips:
    - Always highlight features comparison
    - Lead with the SAVINGS, not the discount
    - Phone script builds trust and professionalism
    - Email provides legal documentation
    - SMS is the follow-up confirmation
    ''')

# Title
'''
# :camera: Promotion Calculator for Customers

Calculate the impact of promotions on customer bills in real-time.
Help your team communicate pricing and savings clearly to customers.
'''

''

# Create two columns for input and results
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader('💰 Customer Bill')
    
    # Customer billing amount input
    customer_bill = st.number_input(
        'Customer Billing Amount ($)',
        min_value=0.0,
        value=5000.0,
        step=100.0,
        format='%.2f'
    )
    
    ''
    
    st.subheader('🎯 Promotion Details')
    
    # Promotion type selection
    promo_type = st.radio(
        'Promotion Type',
        ['Percentage Discount', 'Flat Amount Discount'],
        horizontal=True
    )
    
    if promo_type == 'Percentage Discount':
        promo_value = st.slider(
            'Discount Percentage (%)',
            min_value=0,
            max_value=100,
            value=10,
            step=1
        )
        discount_amount = customer_bill * (promo_value / 100)
    else:
        promo_value = st.number_input(
            'Flat Discount Amount ($)',
            min_value=0.0,
            value=500.0,
            step=50.0,
            format='%.2f'
        )
        discount_amount = min(promo_value, customer_bill)
    
    ''
    
    # Optional promotion code
    promo_code = st.text_input(
        'Promotion Code (optional)',
        placeholder='e.g., SUMMER2026'
    )
    
    ''
    
    st.subheader('📅 Billing Period')
    
    # Bill start date
    bill_start_date = st.date_input(
        'Promotion Start Date',
        value=datetime.today(),
    )

with col2:
    st.subheader('📊 Bill Summary')
    
    # Calculate final bill with taxes and fees
    bill_after_discount = customer_bill - discount_amount
    
    # Tax calculation (example: 8.5%)
    tax_rate = 0.085
    taxes = bill_after_discount * tax_rate
    
    # Processing fee (example: 2.5% or $15, whichever is higher)
    processing_fee = max(15.0, bill_after_discount * 0.025)
    
    final_bill = bill_after_discount + taxes + processing_fee
    
    savings_percent = (discount_amount / customer_bill * 100) if customer_bill > 0 else 0
    
    # Display metrics
    metric_cols = st.columns(3)
    
    with metric_cols[0]:
        st.metric(
            label='Original Bill',
            value=f'${customer_bill:,.2f}',
            delta=None,
        )
    
    with metric_cols[1]:
        st.metric(
            label='Savings',
            value=f'${discount_amount:,.2f}',
            delta=f'{savings_percent:.1f}%',
            delta_color='normal',
        )
    
    with metric_cols[2]:
        st.metric(
            label='Final Bill',
            value=f'${final_bill:,.2f}',
            delta='After all charges',
            delta_color='off',
        )
    
    ''
    ''
    
    # Breakdown table
    st.subheader('Detailed Billing Breakdown')
    
    breakdown_data = {
        'Item': [
            'Original Service Amount',
            'Promotion Discount',
            'Subtotal After Discount',
            'Taxes (8.5%)',
            'Processing Fee',
            'FINAL AMOUNT DUE'
        ],
        'Amount': [
            f'${customer_bill:,.2f}',
            f'-${discount_amount:,.2f}',
            f'${bill_after_discount:,.2f}',
            f'${taxes:,.2f}',
            f'${processing_fee:,.2f}',
            f'${final_bill:,.2f}'
        ]
    }
    
    st.table(breakdown_data)
    
    ''
    
    # Promo code display
    if promo_code:
        st.info(f'✅ Promotion Code Applied: **{promo_code.upper()}**')
    
    ''
    
    # Call to action
    st.success(
        f'💡 **Customer saves ${discount_amount:,.2f}** with this promotion!\n\n'
        f'Effective: {bill_start_date.strftime("%B %d, %Y")}'
    )

''
''
''

# Communications section
st.header('📞 How to Communicate This to Your Customer', divider='blue')

''

# Create tabs for different communication methods
tab1, tab2, tab3 = st.tabs(['📱 SMS Message', '📧 Email Template', '📋 Phone Script'])

with tab1:
    st.subheader('Text Message for Quick Confirmation')
    
    sms_message = f'''Hi [Customer Name]! 🎉

Great news! We have an exclusive promotion for you:

Save ${discount_amount:,.2f} on your account
Your new monthly bill: ${final_bill:,.2f}
Effective: {bill_start_date.strftime('%b %d, %Y')}

{f"Code: {promo_code.upper()}" if promo_code else ""}

Questions? Reply HELP or call us at 1-800-XXX-XXXX'''
    
    st.code(sms_message, language='plaintext')
    
    st.info(f'📊 **Message Length:** {len(sms_message)} characters ({(len(sms_message) // 160) + 1} SMS)')
    
    if st.button('Copy SMS to Clipboard', key='copy_sms'):
        st.success('SMS copied! Paste into your messaging system.')

with tab2:
    st.subheader('Professional Email Template')
    
    email_subject = f"Your Exclusive Promotion - Save ${discount_amount:,.2f}"
    
    email_body = f'''Dear [Customer Name],

We're pleased to offer you an exclusive promotion on your account!

---

PROMOTION DETAILS:

Original Monthly Amount:        ${customer_bill:,.2f}
Promotion Discount:            -${discount_amount:,.2f} ({savings_percent:.1f}%)
───────────────────────────────
Subtotal:                       ${bill_after_discount:,.2f}

Taxes & Fees:
  Taxes (8.5%):               ${taxes:,.2f}
  Processing Fee:             ${processing_fee:,.2f}

───────────────────────────────
YOUR NEW MONTHLY BILL:          ${final_bill:,.2f}

EFFECTIVE DATE:                 {bill_start_date.strftime('%B %d, %Y')}

{f"PROMOTION CODE: {promo_code.upper()}" if promo_code else ""}

---

This promotion is valid for 12 months from the effective date. After that, standard rates will apply. Your account will be updated automatically on {bill_start_date.strftime('%B %d, %Y')}.

If you have any questions or need assistance, please don't hesitate to contact us at:
📞 Phone: 1-800-XXX-XXXX
📧 Email: support@company.com

Thank you for your business!

Best regards,
[Your Name]
[Your Title]
[Company Name]'''
    
    st.code(email_body, language='plaintext')
    
    # Show email subject
    st.info(f'**Subject Line:** {email_subject}')
    
    if st.button('Copy Email to Clipboard', key='copy_email'):
        st.success('Email copied! Paste into your email system.')

with tab3:
    st.subheader('Phone Script for Team')
    
    phone_script = f'''
"Hi [Customer Name], thanks for being a valued customer! I'm calling with some great news.

We have an exclusive promotion for you that'll save you money on your monthly bill.

Here's what we can do for you:

📊 Your current bill is ${customer_bill:,.2f} per month.

With our special promotion, we can reduce that by ${discount_amount:,.2f} ({savings_percent:.1f}%).

That means your new monthly bill would be ${final_bill:,.2f}, which includes:
  • Base charge after discount: ${bill_after_discount:,.2f}
  • Taxes: ${taxes:,.2f}
  • Processing fee: ${processing_fee:,.2f}

So you're looking at a savings of ${discount_amount:,.2f} every single month.

This promotion is effective starting {bill_start_date.strftime('%B %d, %Y')}, and it's valid for a full 12 months.

{f'Your promotion code is: {promo_code.upper()}' if promo_code else 'I can set this up for you right now.'}

Does that work for you? Do you have any questions about the breakdown?"
'''
    
    st.code(phone_script, language='plaintext')
    
    # Key talking points
    st.info('''
    **Key Points to Emphasize:**
    ✅ Monthly savings amount ($)
    ✅ New total bill
    ✅ Effective start date
    ✅ Promotion duration (12 months)
    ✅ What happens after the promotion ends
    ''')

''
''
''

# Footer with instructions
with st.expander('📋 How to use this calculator'):
    st.markdown('''
    ## For Your Phone Team:
    
    1. **Enter the Customer Billing Amount** — This is their current total bill.
    2. **Choose a Promotion Type:**
       - **Percentage Discount** — Apply a percentage off (e.g., 10% off)
       - **Flat Amount Discount** — Apply a fixed dollar discount (e.g., $500 off)
    3. **Set the Promotion Value** — Use the slider or input field to specify the discount.
    4. **Add a Promo Code (optional)** — Enter a code like "SUMMER2026" for tracking.
    5. **Set the Effective Date** — Choose when the promotion starts.
    6. **Use the Communication Templates** — Copy SMS, Email, or Phone Script to communicate with the customer.
    
    ## Real-World Workflow:
    
    - **Step 1:** Call customer → Enter their bill amount
    - **Step 2:** Decide on promotion → Adjust discount %
    - **Step 3:** See final bill instantly
    - **Step 4:** Read the phone script & share the offer
    - **Step 5:** Send them an SMS confirmation with the code
    - **Step 6:** Follow up with detailed email
    
    ## Pro Tips:
    - Compare different discount options before calling (use multiple tabs)
    - Keep the SMS short and actionable
    - Email provides legal documentation
    - Phone script removes guesswork from your team's conversations
    ''')
