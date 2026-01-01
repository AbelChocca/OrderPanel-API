from strawberry.fastapi import GraphQLRouter

graphql_router: GraphQLRouter = GraphQLRouter(
    schema=None,
    path="/graphql", 
    context_getter=None
    )