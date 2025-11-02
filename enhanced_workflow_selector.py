#!/usr/bin/env python3
"""
Enhanced Workflow Selection Tool
Intelligent workflow recommendation system based on project brief analysis.
Inspired by best practices for workflow selection from project briefs.
"""

import re
import sys
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum


class ProjectType(Enum):
    """Project type classification"""
    NEW_PROJECT = "new_project"
    EXISTING_PROJECT = "existing_project"
    FEATURE_ADDITION = "feature_addition"
    REFACTOR = "refactor"
    RESEARCH = "research"
    PRODUCTION = "production"


class ProjectScale(Enum):
    """Project scale classification"""
    SOLO = "solo"
    SMALL_TEAM = "small_team"
    LARGE_TEAM = "large_team"
    ENTERPRISE = "enterprise"


@dataclass
class ProjectRequirements:
    """Structured project requirements"""
    # Core requirements
    knowledge_management: bool = False
    task_tracking: bool = False
    web_crawling: bool = False
    rag_search: bool = False
    agent_development: bool = False
    protocol_based: bool = False
    multi_service: bool = False
    mcp_server: bool = False
    knowledge_graph: bool = False
    documentation: bool = False
    integration: bool = False
    
    # Technical constraints
    python: bool = False
    typescript: bool = False
    react: bool = False
    fastapi: bool = False
    supabase: bool = False
    neo4j: bool = False
    
    # Project characteristics
    project_type: Optional[ProjectType] = None
    project_scale: Optional[ProjectScale] = None
    
    # Specific keywords found
    keywords: List[str] = field(default_factory=list)
    
    # Priority requirements (high/medium/low)
    priority_requirements: Dict[str, str] = field(default_factory=dict)


@dataclass
class WorkflowScore:
    """Workflow recommendation score"""
    workflow_name: str
    total_score: float
    match_percentage: float
    detailed_scores: Dict[str, float]
    reasons: List[str]
    strengths: List[str]
    considerations: List[str]
    recommended: bool = False


class EnhancedWorkflowSelector:
    """Enhanced workflow selector with multi-dimensional analysis"""
    
    def __init__(self):
        self.workflow_capabilities = self._initialize_workflow_capabilities()
        self.scoring_weights = self._initialize_scoring_weights()
    
    def _initialize_workflow_capabilities(self) -> Dict:
        """Initialize detailed workflow capabilities"""
        return {
            'Archon-main': {
                'core_features': {
                    'knowledge_management': {'weight': 10, 'strength': 'excellent'},
                    'task_tracking': {'weight': 10, 'strength': 'excellent'},
                    'rag_search': {'weight': 8, 'strength': 'very_good'},
                    'web_crawling': {'weight': 7, 'strength': 'good'},
                    'mcp_server': {'weight': 9, 'strength': 'excellent'},
                    'documentation': {'weight': 9, 'strength': 'excellent'},
                    'multi_service': {'weight': 10, 'strength': 'excellent'},
                },
                'tech_stack': {
                    'python': {'weight': 8, 'present': True},
                    'typescript': {'weight': 8, 'present': True},
                    'react': {'weight': 7, 'present': True},
                    'fastapi': {'weight': 8, 'present': True},
                    'supabase': {'weight': 9, 'present': True},
                },
                'best_for': [
                    'Knowledge management & documentation systems',
                    'Task tracking and project management',
                    'Multi-agent AI coding workflows',
                    'Real-time collaboration features',
                    'Complex web applications (React + FastAPI)',
                    'Teams needing centralized knowledge base',
                ],
                'not_for': [
                    'Simple single-file scripts',
                    'Pure backend APIs without UI',
                    'Projects without knowledge management needs',
                ],
                'complexity': 'high',
                'setup_time': 'moderate',
                'team_size': 'small_to_large',
            },
            'context-engineering-intro-main': {
                'core_features': {
                    'agent_development': {'weight': 9, 'strength': 'excellent'},
                    'protocol_based': {'weight': 8, 'strength': 'very_good'},
                    'documentation': {'weight': 7, 'strength': 'good'},
                    'mcp_server': {'weight': 8, 'strength': 'very_good'},
                },
                'tech_stack': {
                    'python': {'weight': 9, 'present': True},
                    'typescript': {'weight': 3, 'present': False},
                },
                'best_for': [
                    'New projects starting from scratch',
                    'Context Engineering methodology adoption',
                    'PRP (Product Requirements Prompt) workflow',
                    'Template-based development',
                    'Learning Context Engineering patterns',
                    'Structured feature development',
                ],
                'not_for': [
                    'Existing large codebases',
                    'Simple scripts without structure needs',
                    'Projects already using different methodology',
                ],
                'complexity': 'medium',
                'setup_time': 'quick',
                'team_size': 'solo_to_small',
            },
            'mcp-crawl4ai-rag-main': {
                'core_features': {
                    'web_crawling': {'weight': 10, 'strength': 'excellent'},
                    'rag_search': {'weight': 9, 'strength': 'excellent'},
                    'knowledge_graph': {'weight': 10, 'strength': 'excellent'},
                    'mcp_server': {'weight': 9, 'strength': 'excellent'},
                    'knowledge_management': {'weight': 7, 'strength': 'good'},
                },
                'tech_stack': {
                    'python': {'weight': 10, 'present': True},
                    'supabase': {'weight': 8, 'present': True},
                    'neo4j': {'weight': 10, 'present': True},
                },
                'best_for': [
                    'Web crawling and scraping projects',
                    'Advanced RAG implementations',
                    'Knowledge graph integration',
                    'AI hallucination detection',
                    'Repository code analysis',
                    'MCP server development',
                ],
                'not_for': [
                    'Projects without RAG needs',
                    'Simple CRUD applications',
                    'Projects without web crawling requirements',
                ],
                'complexity': 'high',
                'setup_time': 'moderate',
                'team_size': 'small_to_medium',
            },
            'ottomator-agents-main': {
                'core_features': {
                    'agent_development': {'weight': 10, 'strength': 'excellent'},
                    'integration': {'weight': 9, 'strength': 'excellent'},
                    'rag_search': {'weight': 6, 'strength': 'moderate'},
                    'documentation': {'weight': 5, 'strength': 'moderate'},
                },
                'tech_stack': {
                    'python': {'weight': 9, 'present': True},
                },
                'best_for': [
                    'Specialized agent implementations',
                    'Integration with external services (Airtable, GitHub, Slack)',
                    'RAG agent patterns',
                    'Document processing agents',
                    'Multi-agent systems',
                    'Agent-specific use cases',
                ],
                'not_for': [
                    'Full-stack applications',
                    'Complex multi-service systems',
                    'Projects requiring task management',
                ],
                'complexity': 'medium',
                'setup_time': 'quick',
                'team_size': 'solo_to_small',
            },
            'SuperTemplate-master': {
                'core_features': {
                    'protocol_based': {'weight': 10, 'strength': 'excellent'},
                    'documentation': {'weight': 8, 'strength': 'very_good'},
                },
                'tech_stack': {
                    'python': {'weight': 7, 'present': True},
                },
                'best_for': [
                    'Protocol-based development',
                    'Template generation',
                    'Structured workflow protocols',
                    'Validation systems',
                    'Artifact generation',
                    'Quality gates',
                ],
                'not_for': [
                    'Simple one-off projects',
                    'Projects not requiring protocols',
                    'Rapid prototyping without structure',
                ],
                'complexity': 'high',
                'setup_time': 'moderate',
                'team_size': 'small_to_medium',
            },
        }
    
    def _initialize_scoring_weights(self) -> Dict:
        """Initialize scoring weights for different requirement types"""
        return {
            'core_requirement_match': 3.0,  # High weight for core feature matches
            'tech_stack_match': 2.0,        # Medium weight for tech stack
            'project_type_match': 1.5,      # Medium weight for project type
            'complexity_match': 1.0,        # Low weight for complexity
            'scale_match': 1.0,            # Low weight for team scale
        }
    
    def analyze_project_brief(self, brief: str) -> ProjectRequirements:
        """
        Analyze project brief and extract structured requirements.
        
        Uses multi-level pattern matching and keyword extraction.
        """
        req = ProjectRequirements()
        brief_lower = brief.lower()
        
        # Extract keywords
        req.keywords = self._extract_keywords(brief)
        
        # Core requirements detection
        req.knowledge_management = self._match_patterns(brief_lower, [
            'knowledge', 'documentation', 'docs', 'knowledge base',
            'document management', 'content management', 'knowledge system'
        ])
        
        req.task_tracking = self._match_patterns(brief_lower, [
            'task', 'project management', 'tracking', 'todo',
            'workflow management', 'kanban', 'board', 'task management'
        ])
        
        req.web_crawling = self._match_patterns(brief_lower, [
            'crawl', 'scrape', 'web scraping', 'web crawling',
            'website', 'documentation site', 'crawler'
        ])
        
        req.rag_search = self._match_patterns(brief_lower, [
            'rag', 'retrieval', 'semantic search', 'search',
            'embedding', 'vector', 'similarity search', 'rag search'
        ])
        
        req.agent_development = self._match_patterns(brief_lower, [
            'agent', 'ai agent', 'pydantic ai', 'automation',
            'intelligent agent', 'assistant agent', 'agent system'
        ])
        
        req.protocol_based = self._match_patterns(brief_lower, [
            'protocol', 'template', 'workflow', 'process',
            'structured', 'validation', 'quality gate', 'governance'
        ])
        
        req.multi_service = self._match_patterns(brief_lower, [
            'multi', 'microservice', 'service', 'distributed',
            'multiple services', 'architecture', 'microservices'
        ])
        
        req.mcp_server = self._match_patterns(brief_lower, [
            'mcp', 'model context protocol', 'context protocol'
        ])
        
        req.knowledge_graph = self._match_patterns(brief_lower, [
            'knowledge graph', 'neo4j', 'graph database',
            'graph', 'relationship', 'node', 'graph db'
        ])
        
        req.documentation = self._match_patterns(brief_lower, [
            'documentation', 'docs', 'document', 'readme'
        ])
        
        req.integration = self._match_patterns(brief_lower, [
            'integrate', 'integration', 'airtable', 'github',
            'slack', 'api integration', 'third party', 'external service'
        ])
        
        # Technical stack detection
        req.python = self._match_patterns(brief_lower, ['python', 'python3', 'py'])
        req.typescript = self._match_patterns(brief_lower, ['typescript', 'ts', 'tsx'])
        req.react = self._match_patterns(brief_lower, ['react', 'reactjs', 'react.js'])
        req.fastapi = self._match_patterns(brief_lower, ['fastapi', 'fast api'])
        req.supabase = self._match_patterns(brief_lower, ['supabase'])
        req.neo4j = self._match_patterns(brief_lower, ['neo4j', 'neo 4j'])
        
        # Project type detection
        if self._match_patterns(brief_lower, ['new', 'start', 'begin', 'create', 'build from scratch', 'greenfield']):
            req.project_type = ProjectType.NEW_PROJECT
        elif self._match_patterns(brief_lower, ['existing', 'current', 'legacy', 'already']):
            req.project_type = ProjectType.EXISTING_PROJECT
        elif self._match_patterns(brief_lower, ['add', 'feature', 'enhance', 'extend']):
            req.project_type = ProjectType.FEATURE_ADDITION
        elif self._match_patterns(brief_lower, ['refactor', 'restructure', 'reorganize']):
            req.project_type = ProjectType.REFACTOR
        elif self._match_patterns(brief_lower, ['research', 'explore', 'prototype', 'poc']):
            req.project_type = ProjectType.RESEARCH
        
        # Project scale detection
        if self._match_patterns(brief_lower, ['solo', 'personal', 'individual', 'alone']):
            req.project_scale = ProjectScale.SOLO
        elif self._match_patterns(brief_lower, ['team', 'group', 'collaboration', 'multiple']):
            if self._match_patterns(brief_lower, ['large', 'enterprise', 'organization', 'company']):
                req.project_scale = ProjectScale.ENTERPRISE
            else:
                req.project_scale = ProjectScale.SMALL_TEAM
        
        # Determine priority requirements
        req.priority_requirements = self._determine_priorities(req, brief_lower)
        
        return req
    
    def _match_patterns(self, text: str, patterns: List[str]) -> bool:
        """Check if any pattern matches in text"""
        return any(pattern in text for pattern in patterns)
    
    def _extract_keywords(self, brief: str) -> List[str]:
        """Extract relevant keywords from brief"""
        # Simple keyword extraction - can be enhanced with NLP
        words = re.findall(r'\b\w{4,}\b', brief.lower())
        # Filter common words
        stop_words = {'this', 'that', 'with', 'from', 'have', 'will', 'need', 'want', 'build', 'create'}
        keywords = [w for w in words if w not in stop_words]
        return list(set(keywords))[:20]  # Return top 20 unique keywords
    
    def _determine_priorities(self, req: ProjectRequirements, brief: str) -> Dict[str, str]:
        """Determine priority levels for requirements"""
        priorities = {}
        
        # High priority indicators
        high_priority_keywords = ['critical', 'essential', 'must', 'required', 'priority', 'important']
        if any(kw in brief.lower() for kw in high_priority_keywords):
            # Set high priority for detected requirements
            for attr in dir(req):
                if not attr.startswith('_') and isinstance(getattr(req, attr), bool):
                    if getattr(req, attr):
                        priorities[attr] = 'high'
        
        return priorities
    
    def score_workflow(self, workflow_name: str, requirements: ProjectRequirements) -> WorkflowScore:
        """Calculate multi-dimensional score for a workflow"""
        capabilities = self.workflow_capabilities[workflow_name]
        detailed_scores = {}
        reasons = []
        strengths = []
        considerations = []
        total_score = 0.0
        
        # Score core features
        core_score = 0.0
        core_matches = []
        for feature, capability in capabilities['core_features'].items():
            req_value = getattr(requirements, feature, False)
            if req_value:
                feature_score = capability['weight']
                core_score += feature_score
                core_matches.append(feature)
                reasons.append(f"Requires {feature.replace('_', ' ')} - {workflow_name} provides {capability['strength']} support")
        
        detailed_scores['core_features'] = core_score
        
        # Score tech stack match
        tech_score = 0.0
        tech_matches = []
        for tech, capability in capabilities['tech_stack'].items():
            req_value = getattr(requirements, tech, False)
            if req_value and capability['present']:
                tech_score += capability['weight']
                tech_matches.append(tech)
        
        detailed_scores['tech_stack'] = tech_score
        
        # Score project type match
        type_score = 0.0
        if requirements.project_type == ProjectType.NEW_PROJECT:
            if workflow_name == 'context-engineering-intro-main':
                type_score = 8.0
                reasons.append("Perfect for new projects - template-based approach")
        elif requirements.project_type == ProjectType.EXISTING_PROJECT:
            if workflow_name == 'Archon-main':
                type_score = 7.0
                reasons.append("Suitable for existing projects with knowledge management needs")
        
        detailed_scores['project_type'] = type_score
        
        # Score complexity match
        complexity_score = 0.0
        if requirements.project_scale == ProjectScale.SOLO:
            if capabilities['complexity'] == 'medium' or capabilities['setup_time'] == 'quick':
                complexity_score = 5.0
                reasons.append("Suitable complexity for solo developer")
        elif requirements.project_scale == ProjectScale.ENTERPRISE:
            if capabilities['complexity'] == 'high' or capabilities['team_size'] == 'large_team':
                complexity_score = 5.0
                reasons.append("Suitable for enterprise-scale projects")
        
        detailed_scores['complexity'] = complexity_score
        
        # Calculate total weighted score
        total_score = (
            core_score * self.scoring_weights['core_requirement_match'] +
            tech_score * self.scoring_weights['tech_stack_match'] +
            type_score * self.scoring_weights['project_type_match'] +
            complexity_score * self.scoring_weights['complexity_match']
        )
        
        # Generate strengths and considerations
        strengths = capabilities['best_for'][:3]  # Top 3 strengths
        considerations = capabilities['not_for'][:2]  # Top 2 considerations
        
        # Calculate match percentage (normalize to 0-100)
        max_possible_score = 100.0  # Estimated max score
        match_percentage = min((total_score / max_possible_score) * 100, 100)
        
        # Mark as recommended if score is high enough
        recommended = match_percentage >= 60.0
        
        return WorkflowScore(
            workflow_name=workflow_name,
            total_score=total_score,
            match_percentage=match_percentage,
            detailed_scores=detailed_scores,
            reasons=reasons,
            strengths=strengths,
            considerations=considerations,
            recommended=recommended
        )
    
    def recommend_workflows(self, requirements: ProjectRequirements) -> List[WorkflowScore]:
        """Generate workflow recommendations"""
        scores = []
        
        for workflow_name in self.workflow_capabilities.keys():
            score = self.score_workflow(workflow_name, requirements)
            scores.append(score)
        
        # Sort by total score descending
        scores.sort(key=lambda x: x.total_score, reverse=True)
        
        return scores
    
    def print_recommendations(self, brief: str, requirements: ProjectRequirements, scores: List[WorkflowScore]):
        """Print formatted recommendations"""
        print("=" * 80)
        print("ENHANCED WORKFLOW SELECTION ANALYSIS")
        print("=" * 80)
        
        print("\n📋 Project Brief:")
        print(f"   {brief[:300]}..." if len(brief) > 300 else f"   {brief}")
        
        print("\n🔍 Detected Requirements:")
        detected = []
        for attr in dir(requirements):
            if not attr.startswith('_') and isinstance(getattr(requirements, attr), bool):
                if getattr(requirements, attr):
                    detected.append(attr.replace('_', ' ').title())
        
        if detected:
            for req in detected:
                priority = requirements.priority_requirements.get(attr, 'medium')
                print(f"   ✅ {req} [{priority} priority]")
        else:
            print("   ⚠️  No strong requirements detected")
        
        if requirements.project_type:
            print(f"\n📊 Project Type: {requirements.project_type.value}")
        if requirements.project_scale:
            print(f"👥 Team Scale: {requirements.project_scale.value}")
        
        print("\n🎯 Workflow Recommendations:")
        print()
        
        for i, score in enumerate(scores, 1):
            if score.total_score == 0:
                continue
            
            # Visual score bar
            bar_length = int(score.match_percentage / 5)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            # Recommendation badge
            badge = "⭐ RECOMMENDED" if score.recommended else ""
            
            print(f"{i}. {score.workflow_name} {badge}")
            print(f"   Match Score: {score.match_percentage:.1f}% [{bar}]")
            print(f"   Total Score: {score.total_score:.1f}/100")
            
            # Detailed breakdown
            print(f"\n   📊 Score Breakdown:")
            for category, value in score.detailed_scores.items():
                if value > 0:
                    print(f"      • {category.replace('_', ' ').title()}: {value:.1f}")
            
            # Reasons
            if score.reasons:
                print(f"\n   ✅ Why this workflow:")
                for reason in score.reasons[:3]:  # Top 3 reasons
                    print(f"      • {reason}")
            
            # Strengths
            if score.strengths:
                print(f"\n   💪 Best For:")
                for strength in score.strengths:
                    print(f"      • {strength}")
            
            # Considerations
            if score.considerations:
                print(f"\n   ⚠️  Considerations:")
                for consideration in score.considerations:
                    print(f"      • {consideration}")
            
            print()
        
        # Summary recommendation
        if scores and scores[0].recommended:
            top_workflow = scores[0]
            print("=" * 80)
            print(f"🎯 TOP RECOMMENDATION: {top_workflow.workflow_name}")
            print("=" * 80)
            print(f"\nWith a {top_workflow.match_percentage:.1f}% match score, {top_workflow.workflow_name}")
            print("is the best fit for your project brief.")
            print("\n📚 Next Steps:")
            print(f"   1. Review documentation for {top_workflow.workflow_name}")
            print(f"   2. Check tech stack compatibility")
            print(f"   3. Consider team expertise and learning curve")
            print(f"   4. Start with recommended workflow")
            
            if len(scores) > 1 and scores[1].recommended:
                print(f"\n💡 Alternative: {scores[1].workflow_name} ({scores[1].match_percentage:.1f}% match)")
                print(f"   Consider this if you need: {', '.join(scores[1].strengths[:2])}")
        
        print("\n" + "=" * 80)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python enhanced_workflow_selector.py <project_brief>")
        print("\nExample:")
        print('  python enhanced_workflow_selector.py "Build a knowledge management system for documentation with RAG search"')
        print("\nFor interactive mode:")
        print('  python enhanced_workflow_selector.py --interactive')
        sys.exit(1)
    
    if sys.argv[1] == '--interactive':
        print("=" * 80)
        print("INTERACTIVE WORKFLOW SELECTOR")
        print("=" * 80)
        print("\nPlease describe your project:")
        brief = input("> ")
    else:
        brief = " ".join(sys.argv[1:])
    
    # Initialize selector
    selector = EnhancedWorkflowSelector()
    
    # Analyze brief
    requirements = selector.analyze_project_brief(brief)
    
    # Get recommendations
    scores = selector.recommend_workflows(requirements)
    
    # Print results
    selector.print_recommendations(brief, requirements, scores)
    
    # Optional: Save to JSON
    if '--json' in sys.argv:
        output = {
            'brief': brief,
            'requirements': {
                k: v for k, v in requirements.__dict__.items()
                if not isinstance(v, (list, dict, Enum))
            },
            'recommendations': [
                {
                    'workflow': s.workflow_name,
                    'score': s.total_score,
                    'match_percentage': s.match_percentage,
                    'recommended': s.recommended,
                    'reasons': s.reasons,
                }
                for s in scores
            ]
        }
        print(f"\n💾 Saving analysis to workflow_analysis.json...")
        with open('workflow_analysis.json', 'w') as f:
            json.dump(output, f, indent=2, default=str)


if __name__ == "__main__":
    main()

