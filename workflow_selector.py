#!/usr/bin/env python3
"""
Workflow Selection Tool
Analyzes project briefs and recommends the best workflow from INTEGRATE ecosystem.
"""

import re
import sys
from typing import Dict, List, Tuple


def analyze_project_brief(brief: str) -> Dict[str, bool]:
    """
    Analyze project brief and extract key indicators.
    
    Args:
        brief: Project brief text
    
    Returns:
        Dictionary with extracted requirements and indicators
    """
    indicators = {
        'knowledge_management': False,
        'task_tracking': False,
        'web_crawling': False,
        'rag_search': False,
        'agent_development': False,
        'protocol_based': False,
        'new_project': False,
        'multi_service': False,
        'mcp_server': False,
        'knowledge_graph': False,
        'documentation': False,
        'integration': False,
    }
    
    brief_lower = brief.lower()
    
    # Knowledge management patterns
    knowledge_patterns = [
        'knowledge', 'documentation', 'docs', 'knowledge base',
        'document management', 'content management'
    ]
    if any(pattern in brief_lower for pattern in knowledge_patterns):
        indicators['knowledge_management'] = True
        indicators['documentation'] = True
    
    # Task tracking patterns
    task_patterns = [
        'task', 'project management', 'tracking', 'todo',
        'workflow management', 'kanban', 'board'
    ]
    if any(pattern in brief_lower for pattern in task_patterns):
        indicators['task_tracking'] = True
    
    # Web crawling patterns
    crawl_patterns = [
        'crawl', 'scrape', 'web scraping', 'web crawling',
        'website', 'documentation site'
    ]
    if any(pattern in brief_lower for pattern in crawl_patterns):
        indicators['web_crawling'] = True
    
    # RAG search patterns
    rag_patterns = [
        'rag', 'retrieval', 'semantic search', 'search',
        'embedding', 'vector', 'similarity search'
    ]
    if any(pattern in brief_lower for pattern in rag_patterns):
        indicators['rag_search'] = True
    
    # Agent development patterns
    agent_patterns = [
        'agent', 'ai agent', 'pydantic ai', 'automation',
        'intelligent agent', 'assistant agent'
    ]
    if any(pattern in brief_lower for pattern in agent_patterns):
        indicators['agent_development'] = True
    
    # Protocol-based patterns
    protocol_patterns = [
        'protocol', 'template', 'workflow', 'process',
        'structured', 'validation', 'quality gate'
    ]
    if any(pattern in brief_lower for pattern in protocol_patterns):
        indicators['protocol_based'] = True
    
    # New project patterns
    new_project_patterns = [
        'new', 'start', 'begin', 'create', 'build from scratch',
        'greenfield', 'new project'
    ]
    if any(pattern in brief_lower for pattern in new_project_patterns):
        indicators['new_project'] = True
    
    # Multi-service patterns
    multi_service_patterns = [
        'multi', 'microservice', 'service', 'distributed',
        'multiple services', 'architecture'
    ]
    if any(pattern in brief_lower for pattern in multi_service_patterns):
        indicators['multi_service'] = True
    
    # MCP server patterns
    mcp_patterns = [
        'mcp', 'model context protocol', 'context protocol'
    ]
    if any(pattern in brief_lower for pattern in mcp_patterns):
        indicators['mcp_server'] = True
    
    # Knowledge graph patterns
    kg_patterns = [
        'knowledge graph', 'neo4j', 'graph database',
        'graph', 'relationship', 'node'
    ]
    if any(pattern in brief_lower for pattern in kg_patterns):
        indicators['knowledge_graph'] = True
    
    # Integration patterns
    integration_patterns = [
        'integrate', 'integration', 'airtable', 'github',
        'slack', 'api integration', 'third party'
    ]
    if any(pattern in brief_lower for pattern in integration_patterns):
        indicators['integration'] = True
    
    return indicators


def recommend_workflow(indicators: Dict[str, bool]) -> List[Tuple[str, int, str]]:
    """
    Recommend workflows based on indicators.
    
    Args:
        indicators: Dictionary of detected indicators
    
    Returns:
        List of tuples (workflow_name, score, reason) ordered by score
    """
    scores = {
        'Archon-main': 0,
        'context-engineering-intro-main': 0,
        'mcp-crawl4ai-rag-main': 0,
        'ottomator-agents-main': 0,
        'SuperTemplate-master': 0,
    }
    
    reasons = {
        'Archon-main': [],
        'context-engineering-intro-main': [],
        'mcp-crawl4ai-rag-main': [],
        'ottomator-agents-main': [],
        'SuperTemplate-master': [],
    }
    
    # Archon scoring
    if indicators['knowledge_management']:
        scores['Archon-main'] += 3
        reasons['Archon-main'].append("Knowledge management")
    if indicators['task_tracking']:
        scores['Archon-main'] += 3
        reasons['Archon-main'].append("Task tracking")
    if indicators['multi_service']:
        scores['Archon-main'] += 2
        reasons['Archon-main'].append("Multi-service architecture")
    if indicators['mcp_server']:
        scores['Archon-main'] += 2
        reasons['Archon-main'].append("MCP server")
    if indicators['rag_search']:
        scores['Archon-main'] += 1
        reasons['Archon-main'].append("RAG capabilities")
    if indicators['documentation']:
        scores['Archon-main'] += 2
        reasons['Archon-main'].append("Documentation management")
    
    # Context Engineering scoring
    if indicators['new_project']:
        scores['context-engineering-intro-main'] += 3
        reasons['context-engineering-intro-main'].append("New project")
    if indicators['agent_development']:
        scores['context-engineering-intro-main'] += 2
        reasons['context-engineering-intro-main'].append("Agent development")
    if indicators['protocol_based']:
        scores['context-engineering-intro-main'] += 1
        reasons['context-engineering-intro-main'].append("Structured approach")
    if indicators['documentation']:
        scores['context-engineering-intro-main'] += 1
        reasons['context-engineering-intro-main'].append("Documentation needs")
    
    # Crawl4AI RAG scoring
    if indicators['web_crawling']:
        scores['mcp-crawl4ai-rag-main'] += 3
        reasons['mcp-crawl4ai-rag-main'].append("Web crawling")
    if indicators['rag_search']:
        scores['mcp-crawl4ai-rag-main'] += 2
        reasons['mcp-crawl4ai-rag-main'].append("RAG search")
    if indicators['knowledge_graph']:
        scores['mcp-crawl4ai-rag-main'] += 3
        reasons['mcp-crawl4ai-rag-main'].append("Knowledge graph")
    if indicators['mcp_server']:
        scores['mcp-crawl4ai-rag-main'] += 2
        reasons['mcp-crawl4ai-rag-main'].append("MCP server")
    
    # Ottomator Agents scoring
    if indicators['agent_development']:
        scores['ottomator-agents-main'] += 3
        reasons['ottomator-agents-main'].append("Agent development")
    if indicators['integration']:
        scores['ottomator-agents-main'] += 2
        reasons['ottomator-agents-main'].append("Service integration")
    if indicators['rag_search']:
        scores['ottomator-agents-main'] += 1
        reasons['ottomator-agents-main'].append("RAG capabilities")
    
    # SuperTemplate scoring
    if indicators['protocol_based']:
        scores['SuperTemplate-master'] += 3
        reasons['SuperTemplate-master'].append("Protocol-based")
    if indicators['new_project']:
        scores['SuperTemplate-master'] += 1
        reasons['SuperTemplate-master'].append("New project")
    
    # Create results with reasons
    results = []
    for workflow, score in scores.items():
        if score > 0:
            reason_text = ", ".join(reasons[workflow]) if reasons[workflow] else "Partial match"
            results.append((workflow, score, reason_text))
    
    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results


def print_recommendations(brief: str, indicators: Dict[str, bool], recommendations: List[Tuple[str, int, str]]):
    """Print formatted recommendations."""
    print("=" * 80)
    print("WORKFLOW SELECTION ANALYSIS")
    print("=" * 80)
    print("\n📋 Project Brief:")
    print(f"   {brief[:200]}..." if len(brief) > 200 else f"   {brief}")
    
    print("\n🔍 Detected Indicators:")
    active_indicators = [key for key, value in indicators.items() if value]
    if active_indicators:
        for indicator in active_indicators:
            print(f"   ✅ {indicator.replace('_', ' ').title()}")
    else:
        print("   ⚠️  No strong indicators detected")
    
    print("\n🎯 Recommendations:")
    if recommendations:
        for i, (workflow, score, reason) in enumerate(recommendations, 1):
            percentage = (score / 10) * 100 if score <= 10 else 100
            bar_length = int(percentage / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            print(f"\n   {i}. {workflow}")
            print(f"      Score: {score}/10 ({percentage:.0f}%) [{bar}]")
            print(f"      Reasons: {reason}")
    else:
        print("   ⚠️  No strong recommendations. Consider reviewing project brief.")
    
    print("\n" + "=" * 80)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python workflow_selector.py <project_brief>")
        print("\nExample:")
        print('  python workflow_selector.py "Build a knowledge management system for documentation"')
        sys.exit(1)
    
    brief = " ".join(sys.argv[1:])
    
    # Analyze brief
    indicators = analyze_project_brief(brief)
    
    # Get recommendations
    recommendations = recommend_workflow(indicators)
    
    # Print results
    print_recommendations(brief, indicators, recommendations)
    
    # Print next steps
    if recommendations:
        top_workflow = recommendations[0][0]
        print("\n📚 Next Steps:")
        print(f"   1. Review documentation for {top_workflow}")
        print(f"   2. Check tech stack compatibility")
        print(f"   3. Consider team expertise")
        print(f"   4. Start with recommended workflow")


if __name__ == "__main__":
    main()

