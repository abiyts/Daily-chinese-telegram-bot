import os
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = "330492497"

message = """🇨🇳 DAILY CHINESE LESSON

1. 因为 — yīnwèi — because
🏗️ 因为下雨，所以不能浇筑混凝土。
Because it's raining, we can't cast concrete.

2. 所以 — suǒyǐ — so / therefore
🏗️ 材料还没到，所以不能开始。
The materials haven't arrived, so we can't start.

3. 但是 — dànshì — but
🏗️ 我想开始，但是材料不够。
I want to start, but there aren't enough materials.

4. 或者 — huòzhě — or
🏗️ 今天或者明天浇筑混凝土。
Cast the concrete today or tomorrow.

5. 如果 — rúguǒ — if
🏗️ 如果材料到了，就通知我。
If the materials arrive, inform me.

6. 就 — jiù — then
🏗️ 材料到了，就开始工作。
When the materials arrive, we'll start.

7. 必须 — bìxū — must
🏗️ 今天必须完成。
It must be completed today.

8. 应该 — yīnggāi — should
🏗️ 你应该先检查钢筋。
You should check the rebar first.

9. 需要 — xūyào — need to
🏗️ 我们需要更多钢筋。
We need more rebar.

10. 可以 — kěyǐ — can
🏗️ 现在可以浇筑混凝土。
We can cast concrete now.

📝 Practice:
Translate into Chinese:
“Because the material hasn't arrived, we cannot start.”
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
