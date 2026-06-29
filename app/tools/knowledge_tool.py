from data.support_docs.docs import SUPPORT_DOCS


def search_knowledge_base(category: str):

    return SUPPORT_DOCS.get(category, [])