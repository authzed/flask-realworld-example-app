from arrakisclient.client import ArrakisClient as AuthzedClient
from arrakisclient.types.namespace import ArrakisNamespace as ReferenceableNamespace
from arrakisclient.types.namespace import Relation
from arrakisclient.types.tuple import ArrakisUserset as Userset


class User(ReferenceableNamespace):
    __namespace__ = "thelargeapp/user"

    ellipsis = Relation(relation_name="...")

    def as_authzed_user(self):
        return Userset.from_onr(self.ellipsis)


class Article(ReferenceableNamespace):
    __namespace__ = "thelargeapp/article"

    author = Relation(User)
    can_comment = Relation(User)


token = "tc_backend_client_def_8b5194583577be9fb529eba9599b4aa895d25fa6a5c8043847381c7c4adead83ecc6b1a0b4aaf80c9a48c06be0644b97fcfad903fac2411e0f7acb72f2165835"


def authzed_client():
    return AuthzedClient(Article, User, access_token=token)
