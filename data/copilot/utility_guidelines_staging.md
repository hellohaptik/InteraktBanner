UTILITY TEMPLATE CREATION GUIDELINES (WHATSAPP / MESSENGER / META)

1. DEFINITION AND INTENT
- Utility templates are strictly for transactional, functional, or service-related messages.
- They must be directly tied to a specific user action, request, transaction, or account event.
- They are intended to deliver critical, expected information, not to drive engagement or sales.
- Utility templates are non-promotional by nature.

2. STRICT NON-PROMOTIONAL REQUIREMENT
- No marketing language, sales intent, offers, discounts, coupons, incentives, or upselling.
- No promotional CTAs such as “Buy now”, “Explore more”, “Check out our products”.
- No branding-heavy, persuasive, or benefit-driven language.
- If any marketing intent is detected, the template will be classified as Marketing, regardless of primary purpose.

3. VALID UTILITY USE CASES
Utility templates are allowed only for the following categories:

a. Order and Transaction Updates
- Order confirmations
- Shipping, delivery, or tracking updates
- Delays, cancellations, backorders
- Refunds, returns, or payment status updates

b. Account and Service Notifications
- Account balance updates
- Subscription status or billing reminders
- Policy updates impacting the user
- Security alerts or account-related changes
- Product recalls or safety notices

c. Opt-in and Opt-out Confirmations
- Confirmation of WhatsApp opt-in
- Confirmation of opt-out or preference changes

d. Feedback and Follow-ups (Contextual)
- Feedback requests strictly tied to a completed transaction or interaction
- Post-delivery or post-support experience surveys
- Must not solicit general reviews or promotional engagement

e. Cross-Channel or Support Continuation
- Following up on a support request initiated via another channel
- Case status updates related to prior user contact
- Resolution or progress notifications

4. CONTEXT AND USER EXPECTATION
- The message must be expected by the user.
- The message must clearly reference the triggering event (order, payment, request, case, account).
- Generic or vague messages without clear context are likely to be rejected or reclassified.
- Use specific identifiers (order ID, date, account reference) to establish transactional relevance.

5. VARIABLE USAGE
- Use variables meaningfully to personalize the message to the transaction or event.
- Variables should represent concrete data such as order number, delivery date, amount, account name.
- Templates with placeholders that do not clearly relate to a transaction risk misclassification.

6. LANGUAGE AND TONE
- Neutral, factual, and informative tone.
- No emotional persuasion, excitement, or engagement-driving language.
- No celebratory or marketing-style phrasing.
- Clear, concise, and purpose-driven messaging only.

7. CTA BUTTON RULES
- CTA buttons are allowed only if they support a required transactional action.
- Allowed CTA intents include:
  - View order
  - Track shipment
  - View account
  - Complete required action
  - Contact support (contextual)
- CTA buttons must not redirect to promotional pages or discovery flows.
- Buttons must be essential to completing or understanding the utility message.

8. CONTENT RESTRICTIONS
Utility templates must NOT include:
- Product recommendations
- Promotional links
- Cross-sell or upsell references
- Discounts, offers, or rewards
- Invitations to browse, explore, or shop
- Generic engagement prompts

9. TEMPLATE CATEGORY ENFORCEMENT
- Meta automatically reviews and categorizes templates based on content, not label.
- A utility template containing any marketing or engagement content will be reclassified as Marketing.
- Mixed-intent templates are not allowed; intent must be purely utility.

10. BEST PRACTICES
- Keep the message short, precise, and tied to a single purpose.
- Ensure every sentence supports the transactional intent.
- Avoid unnecessary greetings or closings that add no utility value.
- Make the transactional context immediately clear in the first line.
- Treat guidelines and examples as reference only; do not copy example language directly into templates.

11. DISALLOWED USE OF UTILITY TEMPLATES
Utility templates must not be used for:
- Announcements
- Promotions or campaigns
- Feature launches
- Re-engagement messages
- General brand communication
- Sales or conversion-driven messaging

12. FINAL VALIDATION CHECK
Before submission, confirm:
- The message is expected by the user
- The message is triggered by a real user action or transaction
- The message contains zero promotional intent
- The message content cannot be interpreted as marketing
- The message provides essential, factual information only

UTILITY TEMPLATE EXAMPLES – ACCOUNT CREATION CONFIRMATION

Example 1 (English – en_GB)
Header:
Finalize account set-up

Body:
Hi {{1}},

Your new account has been created successfully.

Please verify {{2}} to complete your profile.

Parameters:
{{1}} = User name
{{2}} = Email address

Button:
- Verify account (URL)

---

Example 2 (French – fr)
Header:
Finalisez la configuration du compte

Body:
Bonjour {{1}},

Votre nouveau compte a été créé correctement.

Veuillez confirmer votre {{2}} pour terminer la configuration de votre profil.

Parameters:
{{1}} = Nom de l’utilisateur
{{2}} = Adresse e-mail

Button:
- Confirmer le compte (URL)

---

Example 3 (Norwegian – nb)
Header:
Fullfør konfigurering av konto

Body:
Hei, {{1}}

Den nye kontoen din er opprettet.

Bekreft {{2}} for å fullføre profilen.

Parameters:
{{1}} = Brukernavn
{{2}} = E-postadresse

Button:
- Bekreft konto (URL)

---

Example 4 (Hindi/Marathi-style regional example – mr)
Header:
खात्याचे सेटअप पूर्ण करा

Body:
नमस्कार {{1}},

तुमचे नवीन खाते तयार झाले आहे.

तुमची प्रोफाइल पूर्ण करण्यासाठी कृपया {{2}} याची पडताळणी करा.

Parameters:
{{1}} = वापरकर्त्याचे नाव
{{2}} = ईमेल पत्ता

Button:
- खात्याची पडताळणी करा (URL)

---

Example 5 (Germanic-language structure – sv)
Header:
Slutför konfiguration av kontot

Body:
Hej {{1}}!

Ditt nya konto har skapats.

Verifiera {{2}} och slutför profilen.

Parameters:
{{1}} = Användarnamn
{{2}} = E-postadress

Button:
- Verifiera konto (URL)

---

Example 6 (Asian-language structure – zh_TW)
Header:
完成帳號設定

Body:
{{1}}您好：

您的新帳號已成功建立。請驗證{{2}}，即可完成個人檔案。

Parameters:
{{1}} = 使用者名稱
{{2}} = 電子郵件地址

Button:
- 驗證帳號 (URL)

---

Example 7 (Middle East – he)
Header:
סיום הגדרת החשבון

Body:
הי {{1}},

סיימת ליצור את החשבון החדש שלך.

כדי להשלים את הפרופיל צריך לאמת את {{2}}.

Parameters:
{{1}} = שם המשתמש
{{2}} = כתובת אימייל

Button:
- אימות החשבון (URL)

---

Example 8 (South-East Asia – vi)
Header:
Hoàn tất quy trình thiết lập tài khoản

Body:
Chào {{1}},

Tài khoản mới của bạn đã được tạo thành công.

Vui lòng xác minh {{2}} để hoàn thiện trang cá nhân của bạn.

Parameters:
{{1}} = Tên người dùng
{{2}} = Địa chỉ email

Button:
- Xác minh tài khoản (URL)

---

COMMON PATTERN OBSERVED ACROSS ALL UTILITY EXAMPLES

- Clear transactional intent: account creation confirmation
- Explicit reference to the triggering event (account creation)
- Use of concrete variables (user name, email address)
- Neutral, factual language
- Single, required CTA to complete the process
- No marketing language, offers, or engagement prompts
- CTA strictly supports completion of a required action
