"""
小学数学作业辅导MCP服务器
支持1-6年级数学题解答和概念讲解

使用方法：
    python -m server

或在Docker中运行：
    docker-compose up
"""

import sys
import logging

if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

from mcp.server.fastmcp import FastMCP

from tools.math_solver import solve_math_problem, explain_math_concept

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("homework_mcp")

mcp = FastMCP("小学数学辅导")

mcp.add_tool(
    solve_math_problem,
    name="solve_math_problem",
    description="""解答小学数学题目。
    当用户问你数学题时使用这个工具。
    支持加减乘除计算题、应用题、分数题、几何题等。
    会返回详细的解题步骤和讲解。"""
)

mcp.add_tool(
    explain_math_concept,
    name="explain_math_concept",
    description="""讲解小学数学概念。
    当用户询问某个数学知识点时使用。
    会用简单易懂的语言解释概念，并举例说明。"""
)

if __name__ == "__main__":
    logger.info("启动小学数学辅导MCP服务器...")
    logger.info("等待小智AI调用工具...")
    mcp.run(transport="stdio")