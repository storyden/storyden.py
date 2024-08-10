# Misc

## Version

Types:

```python
from Storyden.types.misc import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.misc.version.<a href="./src/Storyden/resources/misc/version.py">retrieve</a>() -> str</code>

## OpenAPI

Types:

```python
from Storyden.types.misc import OpenAPIRetrieveResponse
```

Methods:

- <code title="get /openapi.json">client.misc.openapi.<a href="./src/Storyden/resources/misc/openapi.py">retrieve</a>() -> str</code>

## Info

Types:

```python
from Storyden.types.misc import InfoRetrieveResponse
```

Methods:

- <code title="get /v1/info">client.misc.info.<a href="./src/Storyden/resources/misc/info/info.py">retrieve</a>() -> <a href="./src/Storyden/types/misc/info_retrieve_response.py">InfoRetrieveResponse</a></code>

### Icon

Methods:

- <code title="post /v1/info/icon">client.misc.info.icon.<a href="./src/Storyden/resources/misc/info/icon.py">create</a>(\*\*<a href="src/Storyden/types/misc/info/icon_create_params.py">params</a>) -> None</code>
- <code title="get /v1/info/icon/{icon_size}">client.misc.info.icon.<a href="./src/Storyden/resources/misc/info/icon.py">retrieve</a>(icon_size) -> BinaryAPIResponse</code>

# Admin

Types:

```python
from Storyden.types import AdminUpdateResponse
```

Methods:

- <code title="patch /v1/admin">client.admin.<a href="./src/Storyden/resources/admin/admin.py">update</a>(\*\*<a href="src/Storyden/types/admin_update_params.py">params</a>) -> <a href="./src/Storyden/types/admin_update_response.py">AdminUpdateResponse</a></code>

## Bans

Types:

```python
from Storyden.types.admin import BanDeleteSuspendedResponse, BanSuspendResponse
```

Methods:

- <code title="delete /v1/admin/bans/{account_handle}">client.admin.bans.<a href="./src/Storyden/resources/admin/bans.py">delete_suspended</a>(account_handle) -> <a href="./src/Storyden/types/admin/ban_delete_suspended_response.py">BanDeleteSuspendedResponse</a></code>
- <code title="post /v1/admin/bans/{account_handle}">client.admin.bans.<a href="./src/Storyden/resources/admin/bans.py">suspend</a>(account_handle) -> <a href="./src/Storyden/types/admin/ban_suspend_response.py">BanSuspendResponse</a></code>

# Auth

Types:

```python
from Storyden.types import AuthListResponse
```

Methods:

- <code title="get /v1/auth">client.auth.<a href="./src/Storyden/resources/auth/auth.py">list</a>() -> <a href="./src/Storyden/types/auth_list_response.py">AuthListResponse</a></code>
- <code title="get /v1/auth/logout">client.auth.<a href="./src/Storyden/resources/auth/auth.py">logout</a>() -> None</code>

## Password

Types:

```python
from Storyden.types.auth import PasswordCreateResponse, PasswordUpdateResponse, PasswordSigninResponse, PasswordSignupResponse
```

Methods:

- <code title="post /v1/auth/password">client.auth.password.<a href="./src/Storyden/resources/auth/password.py">create</a>(\*\*<a href="src/Storyden/types/auth/password_create_params.py">params</a>) -> <a href="./src/Storyden/types/auth/password_create_response.py">PasswordCreateResponse</a></code>
- <code title="patch /v1/auth/password">client.auth.password.<a href="./src/Storyden/resources/auth/password.py">update</a>(\*\*<a href="src/Storyden/types/auth/password_update_params.py">params</a>) -> <a href="./src/Storyden/types/auth/password_update_response.py">PasswordUpdateResponse</a></code>
- <code title="post /v1/auth/password/signin">client.auth.password.<a href="./src/Storyden/resources/auth/password.py">signin</a>(\*\*<a href="src/Storyden/types/auth/password_signin_params.py">params</a>) -> <a href="./src/Storyden/types/auth/password_signin_response.py">PasswordSigninResponse</a></code>
- <code title="post /v1/auth/password/signup">client.auth.password.<a href="./src/Storyden/resources/auth/password.py">signup</a>(\*\*<a href="src/Storyden/types/auth/password_signup_params.py">params</a>) -> <a href="./src/Storyden/types/auth/password_signup_response.py">PasswordSignupResponse</a></code>

## EmailPassword

Types:

```python
from Storyden.types.auth import EmailPasswordSigninResponse, EmailPasswordSignupResponse
```

Methods:

- <code title="post /v1/auth/email-password/signin">client.auth.email_password.<a href="./src/Storyden/resources/auth/email_password.py">signin</a>(\*\*<a href="src/Storyden/types/auth/email_password_signin_params.py">params</a>) -> <a href="./src/Storyden/types/auth/email_password_signin_response.py">EmailPasswordSigninResponse</a></code>
- <code title="post /v1/auth/email-password/signup">client.auth.email_password.<a href="./src/Storyden/resources/auth/email_password.py">signup</a>(\*\*<a href="src/Storyden/types/auth/email_password_signup_params.py">params</a>) -> <a href="./src/Storyden/types/auth/email_password_signup_response.py">EmailPasswordSignupResponse</a></code>

## Email

Types:

```python
from Storyden.types.auth import EmailSigninResponse, EmailSignupResponse, EmailVerifyResponse
```

Methods:

- <code title="post /v1/auth/email/signin">client.auth.email.<a href="./src/Storyden/resources/auth/email.py">signin</a>(\*\*<a href="src/Storyden/types/auth/email_signin_params.py">params</a>) -> <a href="./src/Storyden/types/auth/email_signin_response.py">EmailSigninResponse</a></code>
- <code title="post /v1/auth/email/signup">client.auth.email.<a href="./src/Storyden/resources/auth/email.py">signup</a>(\*\*<a href="src/Storyden/types/auth/email_signup_params.py">params</a>) -> <a href="./src/Storyden/types/auth/email_signup_response.py">EmailSignupResponse</a></code>
- <code title="post /v1/auth/email/verify">client.auth.email.<a href="./src/Storyden/resources/auth/email.py">verify</a>(\*\*<a href="src/Storyden/types/auth/email_verify_params.py">params</a>) -> <a href="./src/Storyden/types/auth/email_verify_response.py">EmailVerifyResponse</a></code>

## OAuth

Types:

```python
from Storyden.types.auth import OAuthCallbackResponse
```

Methods:

- <code title="post /v1/auth/oauth/{oauth_provider}/callback">client.auth.oauth.<a href="./src/Storyden/resources/auth/oauth.py">callback</a>(oauth_provider, \*\*<a href="src/Storyden/types/auth/oauth_callback_params.py">params</a>) -> <a href="./src/Storyden/types/auth/oauth_callback_response.py">OAuthCallbackResponse</a></code>

## Webauthn

Types:

```python
from Storyden.types.auth import WebauthnMakeResponse
```

Methods:

- <code title="post /v1/auth/webauthn/make">client.auth.webauthn.<a href="./src/Storyden/resources/auth/webauthn/webauthn.py">make</a>(\*\*<a href="src/Storyden/types/auth/webauthn_make_params.py">params</a>) -> <a href="./src/Storyden/types/auth/webauthn_make_response.py">WebauthnMakeResponse</a></code>

### Assert

Types:

```python
from Storyden.types.auth.webauthn import AssertStartResponse
```

Methods:

- <code title="get /v1/auth/webauthn/assert/{account_handle}">client.auth.webauthn.assert*.<a href="./src/Storyden/resources/auth/webauthn/assert*.py">start</a>(account_handle) -> <a href="./src/Storyden/types/auth/webauthn/assert_start_response.py">AssertStartResponse</a></code>

## Phone

Types:

```python
from Storyden.types.auth import PhoneCompleteResponse, PhoneStartResponse
```

Methods:

- <code title="put /v1/auth/phone/{account_handle}">client.auth.phone.<a href="./src/Storyden/resources/auth/phone.py">complete</a>(account_handle, \*\*<a href="src/Storyden/types/auth/phone_complete_params.py">params</a>) -> <a href="./src/Storyden/types/auth/phone_complete_response.py">PhoneCompleteResponse</a></code>
- <code title="post /v1/auth/phone">client.auth.phone.<a href="./src/Storyden/resources/auth/phone.py">start</a>(\*\*<a href="src/Storyden/types/auth/phone_start_params.py">params</a>) -> <a href="./src/Storyden/types/auth/phone_start_response.py">PhoneStartResponse</a></code>

# Accounts

Types:

```python
from Storyden.types import AccountUpdateResponse, AccountListResponse
```

Methods:

- <code title="patch /v1/accounts">client.accounts.<a href="./src/Storyden/resources/accounts/accounts.py">update</a>(\*\*<a href="src/Storyden/types/account_update_params.py">params</a>) -> <a href="./src/Storyden/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /v1/accounts">client.accounts.<a href="./src/Storyden/resources/accounts/accounts.py">list</a>() -> <a href="./src/Storyden/types/account_list_response.py">AccountListResponse</a></code>

## Self

### AuthMethods

Types:

```python
from Storyden.types.accounts.self import AuthMethodListResponse, AuthMethodDeleteResponse
```

Methods:

- <code title="get /v1/accounts/self/auth-methods">client.accounts.self.auth_methods.<a href="./src/Storyden/resources/accounts/self/auth_methods.py">list</a>() -> <a href="./src/Storyden/types/accounts/self/auth_method_list_response.py">AuthMethodListResponse</a></code>
- <code title="delete /v1/accounts/self/auth-methods/{auth_method_id}">client.accounts.self.auth_methods.<a href="./src/Storyden/resources/accounts/self/auth_methods.py">delete</a>(auth_method_id) -> <a href="./src/Storyden/types/accounts/self/auth_method_delete_response.py">AuthMethodDeleteResponse</a></code>

### Avatar

Methods:

- <code title="post /v1/accounts/self/avatar">client.accounts.self.avatar.<a href="./src/Storyden/resources/accounts/self/avatar.py">create</a>(\*\*<a href="src/Storyden/types/accounts/self/avatar_create_params.py">params</a>) -> None</code>

## Avatar

Methods:

- <code title="get /v1/accounts/{account_handle}/avatar">client.accounts.avatar.<a href="./src/Storyden/resources/accounts/avatar.py">retrieve</a>(account_handle) -> BinaryAPIResponse</code>

# Profiles

Types:

```python
from Storyden.types import ProfileRetrieveResponse, ProfileListResponse
```

Methods:

- <code title="get /v1/profiles/{account_handle}">client.profiles.<a href="./src/Storyden/resources/profiles.py">retrieve</a>(account_handle) -> <a href="./src/Storyden/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="get /v1/profiles">client.profiles.<a href="./src/Storyden/resources/profiles.py">list</a>(\*\*<a href="src/Storyden/types/profile_list_params.py">params</a>) -> <a href="./src/Storyden/types/profile_list_response.py">ProfileListResponse</a></code>

# Categories

Types:

```python
from Storyden.types import CategoryCreateResponse, CategoryUpdateResponse, CategoryListResponse
```

Methods:

- <code title="post /v1/categories">client.categories.<a href="./src/Storyden/resources/categories.py">create</a>(\*\*<a href="src/Storyden/types/category_create_params.py">params</a>) -> <a href="./src/Storyden/types/category_create_response.py">CategoryCreateResponse</a></code>
- <code title="patch /v1/categories/{category_id}">client.categories.<a href="./src/Storyden/resources/categories.py">update</a>(category_id, \*\*<a href="src/Storyden/types/category_update_params.py">params</a>) -> <a href="./src/Storyden/types/category_update_response.py">CategoryUpdateResponse</a></code>
- <code title="get /v1/categories">client.categories.<a href="./src/Storyden/resources/categories.py">list</a>() -> <a href="./src/Storyden/types/category_list_response.py">CategoryListResponse</a></code>

# Threads

Types:

```python
from Storyden.types import ThreadCreateResponse, ThreadRetrieveResponse, ThreadUpdateResponse, ThreadListResponse
```

Methods:

- <code title="post /v1/threads">client.threads.<a href="./src/Storyden/resources/threads/threads.py">create</a>(\*\*<a href="src/Storyden/types/thread_create_params.py">params</a>) -> <a href="./src/Storyden/types/thread_create_response.py">ThreadCreateResponse</a></code>
- <code title="get /v1/threads/{thread_mark}">client.threads.<a href="./src/Storyden/resources/threads/threads.py">retrieve</a>(thread_mark) -> <a href="./src/Storyden/types/thread_retrieve_response.py">ThreadRetrieveResponse</a></code>
- <code title="patch /v1/threads/{thread_mark}">client.threads.<a href="./src/Storyden/resources/threads/threads.py">update</a>(thread_mark, \*\*<a href="src/Storyden/types/thread_update_params.py">params</a>) -> <a href="./src/Storyden/types/thread_update_response.py">ThreadUpdateResponse</a></code>
- <code title="get /v1/threads">client.threads.<a href="./src/Storyden/resources/threads/threads.py">list</a>(\*\*<a href="src/Storyden/types/thread_list_params.py">params</a>) -> <a href="./src/Storyden/types/thread_list_response.py">ThreadListResponse</a></code>
- <code title="delete /v1/threads/{thread_mark}">client.threads.<a href="./src/Storyden/resources/threads/threads.py">delete</a>(thread_mark) -> None</code>

# Posts

Types:

```python
from Storyden.types import PostUpdateResponse, PostSearchResponse
```

Methods:

- <code title="patch /v1/posts/{post_id}">client.posts.<a href="./src/Storyden/resources/posts/posts.py">update</a>(post_id, \*\*<a href="src/Storyden/types/post_update_params.py">params</a>) -> <a href="./src/Storyden/types/post_update_response.py">PostUpdateResponse</a></code>
- <code title="delete /v1/posts/{post_id}">client.posts.<a href="./src/Storyden/resources/posts/posts.py">delete</a>(post_id) -> None</code>
- <code title="get /v1/posts/search">client.posts.<a href="./src/Storyden/resources/posts/posts.py">search</a>(\*\*<a href="src/Storyden/types/post_search_params.py">params</a>) -> <a href="./src/Storyden/types/post_search_response.py">PostSearchResponse</a></code>

## Reacts

Types:

```python
from Storyden.types.posts import ReactUpdateResponse
```

Methods:

- <code title="put /v1/posts/{post_id}/reacts">client.posts.reacts.<a href="./src/Storyden/resources/posts/reacts.py">update</a>(post_id, \*\*<a href="src/Storyden/types/posts/react_update_params.py">params</a>) -> <a href="./src/Storyden/types/posts/react_update_response.py">ReactUpdateResponse</a></code>

# Assets

Types:

```python
from Storyden.types import AssetCreateResponse
```

Methods:

- <code title="post /v1/assets">client.assets.<a href="./src/Storyden/resources/assets.py">create</a>(\*\*<a href="src/Storyden/types/asset_create_params.py">params</a>) -> <a href="./src/Storyden/types/asset_create_response.py">AssetCreateResponse</a></code>
- <code title="get /v1/assets/{asset_filename}">client.assets.<a href="./src/Storyden/resources/assets.py">retrieve</a>(asset_filename) -> BinaryAPIResponse</code>

# Collections

Types:

```python
from Storyden.types import CollectionCreateResponse, CollectionRetrieveResponse, CollectionUpdateResponse, CollectionListResponse
```

Methods:

- <code title="post /v1/collections">client.collections.<a href="./src/Storyden/resources/collections/collections.py">create</a>(\*\*<a href="src/Storyden/types/collection_create_params.py">params</a>) -> <a href="./src/Storyden/types/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="get /v1/collections/{collection_id}">client.collections.<a href="./src/Storyden/resources/collections/collections.py">retrieve</a>(collection_id) -> <a href="./src/Storyden/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>
- <code title="patch /v1/collections/{collection_id}">client.collections.<a href="./src/Storyden/resources/collections/collections.py">update</a>(collection_id, \*\*<a href="src/Storyden/types/collection_update_params.py">params</a>) -> <a href="./src/Storyden/types/collection_update_response.py">CollectionUpdateResponse</a></code>
- <code title="get /v1/collections">client.collections.<a href="./src/Storyden/resources/collections/collections.py">list</a>(\*\*<a href="src/Storyden/types/collection_list_params.py">params</a>) -> <a href="./src/Storyden/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /v1/collections/{collection_id}">client.collections.<a href="./src/Storyden/resources/collections/collections.py">delete</a>(collection_id) -> None</code>

## Posts

Types:

```python
from Storyden.types.collections import PostAddResponse, PostRemoveResponse
```

Methods:

- <code title="put /v1/collections/{collection_id}/posts/{post_id}">client.collections.posts.<a href="./src/Storyden/resources/collections/posts.py">add</a>(post_id, \*, collection_id) -> <a href="./src/Storyden/types/collections/post_add_response.py">PostAddResponse</a></code>
- <code title="delete /v1/collections/{collection_id}/posts/{post_id}">client.collections.posts.<a href="./src/Storyden/resources/collections/posts.py">remove</a>(post_id, \*, collection_id) -> <a href="./src/Storyden/types/collections/post_remove_response.py">PostRemoveResponse</a></code>

## Nodes

Types:

```python
from Storyden.types.collections import NodeAddResponse, NodeRemoveResponse
```

Methods:

- <code title="put /v1/collections/{collection_id}/nodes/{node_id}">client.collections.nodes.<a href="./src/Storyden/resources/collections/nodes.py">add</a>(node_id, \*, collection_id) -> <a href="./src/Storyden/types/collections/node_add_response.py">NodeAddResponse</a></code>
- <code title="delete /v1/collections/{collection_id}/nodes/{node_id}">client.collections.nodes.<a href="./src/Storyden/resources/collections/nodes.py">remove</a>(node_id, \*, collection_id) -> <a href="./src/Storyden/types/collections/node_remove_response.py">NodeRemoveResponse</a></code>

# Nodes

Types:

```python
from Storyden.types import NodeCreateResponse, NodeRetrieveResponse, NodeUpdateResponse, NodeListResponse, NodeDeleteResponse
```

Methods:

- <code title="post /v1/nodes">client.nodes.<a href="./src/Storyden/resources/nodes/nodes.py">create</a>(\*\*<a href="src/Storyden/types/node_create_params.py">params</a>) -> <a href="./src/Storyden/types/node_create_response.py">NodeCreateResponse</a></code>
- <code title="get /v1/nodes/{node_slug}">client.nodes.<a href="./src/Storyden/resources/nodes/nodes.py">retrieve</a>(node_slug) -> <a href="./src/Storyden/types/node_retrieve_response.py">NodeRetrieveResponse</a></code>
- <code title="patch /v1/nodes/{node_slug}">client.nodes.<a href="./src/Storyden/resources/nodes/nodes.py">update</a>(node_slug, \*\*<a href="src/Storyden/types/node_update_params.py">params</a>) -> <a href="./src/Storyden/types/node_update_response.py">NodeUpdateResponse</a></code>
- <code title="get /v1/nodes">client.nodes.<a href="./src/Storyden/resources/nodes/nodes.py">list</a>(\*\*<a href="src/Storyden/types/node_list_params.py">params</a>) -> <a href="./src/Storyden/types/node_list_response.py">NodeListResponse</a></code>
- <code title="delete /v1/nodes/{node_slug}">client.nodes.<a href="./src/Storyden/resources/nodes/nodes.py">delete</a>(node_slug, \*\*<a href="src/Storyden/types/node_delete_params.py">params</a>) -> <a href="./src/Storyden/types/node_delete_response.py">NodeDeleteResponse</a></code>

## Visibility

Types:

```python
from Storyden.types.nodes import VisibilityUpdateResponse
```

Methods:

- <code title="patch /v1/nodes/{node_slug}/visibility">client.nodes.visibility.<a href="./src/Storyden/resources/nodes/visibility.py">update</a>(node_slug, \*\*<a href="src/Storyden/types/nodes/visibility_update_params.py">params</a>) -> <a href="./src/Storyden/types/nodes/visibility_update_response.py">VisibilityUpdateResponse</a></code>

## Assets

Types:

```python
from Storyden.types.nodes import AssetAddResponse, AssetRemoveResponse
```

Methods:

- <code title="put /v1/nodes/{node_slug}/assets/{asset_id}">client.nodes.assets.<a href="./src/Storyden/resources/nodes/assets.py">add</a>(asset_id, \*, node_slug, \*\*<a href="src/Storyden/types/nodes/asset_add_params.py">params</a>) -> <a href="./src/Storyden/types/nodes/asset_add_response.py">AssetAddResponse</a></code>
- <code title="delete /v1/nodes/{node_slug}/assets/{asset_id}">client.nodes.assets.<a href="./src/Storyden/resources/nodes/assets.py">remove</a>(asset_id, \*, node_slug) -> <a href="./src/Storyden/types/nodes/asset_remove_response.py">AssetRemoveResponse</a></code>

## Children

Types:

```python
from Storyden.types.nodes import ChildRemoveParentResponse, ChildSetParentResponse
```

Methods:

- <code title="delete /v1/nodes/{node_slug}/nodes/{node_slug_child}">client.nodes.children.<a href="./src/Storyden/resources/nodes/children.py">remove_parent</a>(node_slug_child, \*, node_slug) -> <a href="./src/Storyden/types/nodes/child_remove_parent_response.py">ChildRemoveParentResponse</a></code>
- <code title="put /v1/nodes/{node_slug}/nodes/{node_slug_child}">client.nodes.children.<a href="./src/Storyden/resources/nodes/children.py">set_parent</a>(node_slug_child, \*, node_slug) -> <a href="./src/Storyden/types/nodes/child_set_parent_response.py">ChildSetParentResponse</a></code>

# Links

Types:

```python
from Storyden.types import LinkCreateResponse, LinkRetrieveResponse, LinkListResponse
```

Methods:

- <code title="post /v1/links">client.links.<a href="./src/Storyden/resources/links.py">create</a>(\*\*<a href="src/Storyden/types/link_create_params.py">params</a>) -> <a href="./src/Storyden/types/link_create_response.py">LinkCreateResponse</a></code>
- <code title="get /v1/links/{link_slug}">client.links.<a href="./src/Storyden/resources/links.py">retrieve</a>(link_slug) -> <a href="./src/Storyden/types/link_retrieve_response.py">LinkRetrieveResponse</a></code>
- <code title="get /v1/links">client.links.<a href="./src/Storyden/resources/links.py">list</a>(\*\*<a href="src/Storyden/types/link_list_params.py">params</a>) -> <a href="./src/Storyden/types/link_list_response.py">LinkListResponse</a></code>

# Datagraph

Types:

```python
from Storyden.types import DatagraphListResponse
```

Methods:

- <code title="get /v1/datagraph">client.datagraph.<a href="./src/Storyden/resources/datagraph.py">list</a>(\*\*<a href="src/Storyden/types/datagraph_list_params.py">params</a>) -> <a href="./src/Storyden/types/datagraph_list_response.py">DatagraphListResponse</a></code>
