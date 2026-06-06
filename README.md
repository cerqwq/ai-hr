# 👥 AI HR

AI人力资源工具，支持招聘、培训、绩效管理。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📋 职位描述生成
- 📄 简历筛选
- ❓ 面试题生成
- 📚 培训计划
- 📊 绩效评估
- 💰 薪酬计算

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_hr import create_tools

tools = create_tools()

# 职位描述
jd = tools.generate_job_description("Python开发", requirements)

# 简历筛选
screening = tools.screen_resume(resume, job_requirements)

# 面试题
questions = tools.generate_interview_questions("Python开发", ["Python", "FastAPI"])

# 培训计划
training = tools.create_training_plan("开发工程师", ["沟通", "项目管理"])

# 绩效评估
review = tools.generate_performance_review(employee_data)

# 薪酬计算
compensation = tools.calculate_compensation("Python开发", "3年", "北京")
```

## 📁 项目结构

```
ai-hr/
├── tools.py       # HR工具核心
└── README.md
```

## 📄 许可证

MIT License
