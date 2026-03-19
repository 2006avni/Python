from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_invoice(customer, items, total):

    filename = f"Invoice_{customer}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 22)
    c.drawString(220, height - 60, "INVOICE")

    # Customer info
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 120, f"Customer Name: {customer}")
    c.drawString(50, height - 140, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

    # Table Header
    c.setFont("Helvetica-Bold", 12)

    c.drawString(50, height - 200, "Item")
    c.drawString(250, height - 200, "Quantity")
    c.drawString(350, height - 200, "Price")

    y = height - 230

    c.setFont("Helvetica", 12)

    for item in items:

        c.drawString(50, y, item["name"])
        c.drawString(250, y, str(item["qty"]))
        c.drawString(350, y, f"₹ {item['price']}")

        y -= 25

    # Total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 20, f"Total Amount: ₹ {total}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(200, 60, "Thank you for shopping with us!")

    c.save()

    print(f"\n✅ Invoice Generated: {filename}")
