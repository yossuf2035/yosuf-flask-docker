# استخدم صورة Python الرسمية كأساس
FROM python:3.10-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى داخل الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --upgrade pip && pip install -r requirements.txt

# تشغيل التطبيق
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]