from unstructured.partition.pdf import partition_pdf

pdf_path = "rag.pdf"

print("使用 hi_res 策略解析:")
elements_hi_res = partition_pdf(
    filename=pdf_path,
    strategy="hi_res"
)

# 打印解析结果
print(f"解析完成：{len(elements_hi_res)} 个元素， {sum(len(str(e)) for e in elements_hi_res)} 字符")

# 统计元素类型
from collections import Counter
types_hi_res = Counter(e.category for e in elements_hi_res)
print(f"元素类型: {dict(types_hi_res)}")

print("\n使用 ocr_only 策略解析:")
elements_ocr_only = partition_pdf(
    filename=pdf_path,
    strategy="ocr_only"
)

# 打印解析结果
print(f"解析完成：{len(elements_ocr_only)} 个元素， {sum(len(str(e)) for e in elements_ocr_only)} 字符")

# 统计元素类型
types_ocr_only = Counter(e.category for e in elements_ocr_only)
print(f"元素类型: {dict(types_ocr_only)}")

# 显示hi_res策略的所有元素
print("\nhi_res 策略解析的所有元素:")
for i, element in enumerate(elements_hi_res, 1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)

# 显示ocr_only策略的所有元素
print("\nocr_only 策略解析的所有元素:")
for i, element in enumerate(elements_ocr_only, 1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)
