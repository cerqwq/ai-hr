"""
AI HR - AI人力资源工具
支持招聘、培训、绩效管理
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIHRTools:
    """
    AI人力资源工具
    支持：招聘、培训、绩效
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_job_description(self, position: str, requirements: Dict) -> str:
        """生成职位描述"""
        if not self.client:
            return "LLM客户端未配置"

        req_text = json.dumps(requirements, ensure_ascii=False)

        prompt = f"""请生成{position}的职位描述：

要求：{req_text}

包含：
1. 职位概述
2. 工作职责
3. 任职要求
4. 福利待遇"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def screen_resume(self, resume: str, job_requirements: str) -> Dict:
        """筛选简历"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请根据以下要求筛选简历：

职位要求：{job_requirements}

简历：
{resume[:1500]}

请返回JSON格式：
{{
    "match_score": 1-100,
    "strengths": ["优势"],
    "gaps": ["不足"],
    "recommendation": "interview/maybe/reject",
    "questions": ["建议提问"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"screening": content}

    def generate_interview_questions(self, position: str, skills: List[str]) -> List[Dict]:
        """生成面试题"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        skills_text = ", ".join(skills)

        prompt = f"""请为{position}岗位生成面试题：

技能要求：{skills_text}

请返回JSON格式：
[
    {{"question": "问题", "type": "技术/行为/情景", "expected_answer": "参考答案", "evaluation": "评估标准"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"questions": content}]

    def create_training_plan(self, employee_role: str, skill_gaps: List[str]) -> Dict:
        """创建培训计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        gaps_text = ", ".join(skill_gaps)

        prompt = f"""请为{employee_role}创建培训计划：

技能差距：{gaps_text}

请返回JSON格式：
{{
    "modules": [
        {{"name": "模块名", "duration": "时长", "topics": ["主题"], "method": "培训方式"}}
    ],
    "milestones": ["里程碑"],
    "assessment": "评估方式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"training": content}

    def generate_performance_review(self, employee_data: Dict) -> str:
        """生成绩效评估"""
        if not self.client:
            return "LLM客户端未配置"

        data_text = json.dumps(employee_data, ensure_ascii=False)

        prompt = f"""请根据以下数据生成绩效评估：

{data_text}

要求：
1. 客观公正
2. 具体事例
3. 改进建议
4. 发展计划"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def calculate_compensation(self, position: str, experience: str, location: str) -> Dict:
        """计算薪酬"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请估算{location}的{position}薪酬（{experience}经验）：

请返回JSON格式：
{{
    "base_salary": {{"min": "最低", "max": "最高", "median": "中位数"}},
    "bonus": "奖金范围",
    "benefits": ["福利"],
    "total_compensation": "总薪酬范围"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"compensation": content}


def create_tools(**kwargs) -> AIHRTools:
    """创建HR工具"""
    return AIHRTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI HR Tools")
    print()

    # 测试
    jd = tools.generate_job_description("Python开发", {"经验": "3年", "技能": ["Python", "FastAPI"]})
    print(jd[:300] + "...")
