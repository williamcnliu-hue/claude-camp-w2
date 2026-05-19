# 文本词频统计器
# Week 2 Exercise 2 - Word Frequency Counter

print("=== 文本词频统计器 ===")
print("请输入一段英文文字（输入完按回车）：")
text = input()

# 1. 把整段文字变成全小写（忽略大小写差异）
text = text.lower()

# 2. 把文字按空格切成一个个单词
words = text.split()

# 3. 用字典统计每个单词出现的次数
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

# 4. 按次数从高到低排序
# sorted() 是Python内置工具，items()把字典变成键值对列表
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 5. 输出结果
print(f"\n📊 词频统计结果（共 {len(word_count)} 个不同单词）：")
print("-" * 40)
for word, count in sorted_words:
    print(f"  {word}: {count} 次")
    