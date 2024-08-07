# Version

Types:

```python
from storyden.types import VersionRetrieveResponse
```

Methods:

- <code title="get /version">client.version.<a href="./src/storyden/resources/version.py">retrieve</a>() -> str</code>

# OpenAPIJson

Types:

```python
from storyden.types import OpenAPIJsonRetrieveResponse
```

Methods:

- <code title="get /openapi.json">client.openapi_json.<a href="./src/storyden/resources/openapi_json.py">retrieve</a>() -> str</code>

# V1

## Info

Types:

```python
from storyden.types.v1 import InfoListResponse
```

Methods:

- <code title="get /v1/info">client.v1.info.<a href="./src/storyden/resources/v1/info/info.py">list</a>() -> <a href="./src/storyden/types/v1/info_list_response.py">InfoListResponse</a></code>

### Icon

Methods:

- <code title="post /v1/info/icon">client.v1.info.icon.<a href="./src/storyden/resources/v1/info/icon.py">create</a>(\*\*<a href="src/storyden/types/v1/info/icon_create_params.py">params</a>) -> None</code>
- <code title="get /v1/info/icon/{icon_size}">client.v1.info.icon.<a href="./src/storyden/resources/v1/info/icon.py">retrieve</a>(icon_size) -> BinaryAPIResponse</code>

## Admin

Types:

```python
from storyden.types.v1 import AdminUpdateResponse
```

Methods:

- <code title="patch /v1/admin">client.v1.admin.<a href="./src/storyden/resources/v1/admin/admin.py">update</a>(\*\*<a href="src/storyden/types/v1/admin_update_params.py">params</a>) -> <a href="./src/storyden/types/v1/admin_update_response.py">AdminUpdateResponse</a></code>

### Bans

Types:

```python
from storyden.types.v1.admin import BanCreateResponse, BanDeleteResponse
```

Methods:

- <code title="post /v1/admin/bans/{account_handle}">client.v1.admin.bans.<a href="./src/storyden/resources/v1/admin/bans.py">create</a>(account_handle) -> <a href="./src/storyden/types/v1/admin/ban_create_response.py">BanCreateResponse</a></code>
- <code title="delete /v1/admin/bans/{account_handle}">client.v1.admin.bans.<a href="./src/storyden/resources/v1/admin/bans.py">delete</a>(account_handle) -> <a href="./src/storyden/types/v1/admin/ban_delete_response.py">BanDeleteResponse</a></code>

## Auth

Types:

```python
from storyden.types.v1 import AuthListResponse, AuthPasswordSignupResponse
```

Methods:

- <code title="get /v1/auth">client.v1.auth.<a href="./src/storyden/resources/v1/auth.py">list</a>() -> <a href="./src/storyden/types/v1/auth_list_response.py">AuthListResponse</a></code>
- <code title="get /v1/auth/logout">client.v1.auth.<a href="./src/storyden/resources/v1/auth.py">logout</a>() -> None</code>
- <code title="post /v1/auth/password/signup">client.v1.auth.<a href="./src/storyden/resources/v1/auth.py">password_signup</a>(\*\*<a href="src/storyden/types/v1/auth_password_signup_params.py">params</a>) -> <a href="./src/storyden/types/v1/auth_password_signup_response.py">AuthPasswordSignupResponse</a></code>

## Accounts

Types:

```python
from storyden.types.v1 import AccountRetrieveResponse, AccountUpdateResponse
```

Methods:

- <code title="get /v1/accounts">client.v1.accounts.<a href="./src/storyden/resources/v1/accounts/accounts.py">retrieve</a>() -> <a href="./src/storyden/types/v1/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="patch /v1/accounts">client.v1.accounts.<a href="./src/storyden/resources/v1/accounts/accounts.py">update</a>(\*\*<a href="src/storyden/types/v1/account_update_params.py">params</a>) -> <a href="./src/storyden/types/v1/account_update_response.py">AccountUpdateResponse</a></code>

### AuthMethods

Types:

```python
from storyden.types.v1.accounts import AuthMethodListResponse, AuthMethodDeleteResponse
```

Methods:

- <code title="get /v1/accounts/self/auth-methods">client.v1.accounts.auth_methods.<a href="./src/storyden/resources/v1/accounts/auth_methods.py">list</a>() -> <a href="./src/storyden/types/v1/accounts/auth_method_list_response.py">AuthMethodListResponse</a></code>
- <code title="delete /v1/accounts/self/auth-methods/{auth_method_id}">client.v1.accounts.auth_methods.<a href="./src/storyden/resources/v1/accounts/auth_methods.py">delete</a>(auth_method_id) -> <a href="./src/storyden/types/v1/accounts/auth_method_delete_response.py">AuthMethodDeleteResponse</a></code>

### Avatar

Methods:

- <code title="post /v1/accounts/self/avatar">client.v1.accounts.avatar.<a href="./src/storyden/resources/v1/accounts/avatar.py">create</a>(\*\*<a href="src/storyden/types/v1/accounts/avatar_create_params.py">params</a>) -> None</code>
- <code title="get /v1/accounts/{account_handle}/avatar">client.v1.accounts.avatar.<a href="./src/storyden/resources/v1/accounts/avatar.py">retrieve</a>(account_handle) -> BinaryAPIResponse</code>

## Profiles

Types:

```python
from storyden.types.v1 import ProfileRetrieveResponse, ProfileListResponse
```

Methods:

- <code title="get /v1/profiles/{account_handle}">client.v1.profiles.<a href="./src/storyden/resources/v1/profiles.py">retrieve</a>(account_handle) -> <a href="./src/storyden/types/v1/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="get /v1/profiles">client.v1.profiles.<a href="./src/storyden/resources/v1/profiles.py">list</a>(\*\*<a href="src/storyden/types/v1/profile_list_params.py">params</a>) -> <a href="./src/storyden/types/v1/profile_list_response.py">ProfileListResponse</a></code>

## Categories

Types:

```python
from storyden.types.v1 import CategoryCreateResponse
```

Methods:

- <code title="post /v1/categories">client.v1.categories.<a href="./src/storyden/resources/v1/categories.py">create</a>(\*\*<a href="src/storyden/types/v1/category_create_params.py">params</a>) -> <a href="./src/storyden/types/v1/category_create_response.py">CategoryCreateResponse</a></code>

# Auth

## Password

Types:

```python
from storyden.types.auth import (
    PasswordCreateResponse,
    PasswordUpdateResponse,
    PasswordSigninResponse,
)
```

Methods:

- <code title="post /v1/auth/password">client.auth.password.<a href="./src/storyden/resources/auth/password.py">create</a>(\*\*<a href="src/storyden/types/auth/password_create_params.py">params</a>) -> <a href="./src/storyden/types/auth/password_create_response.py">PasswordCreateResponse</a></code>
- <code title="patch /v1/auth/password">client.auth.password.<a href="./src/storyden/resources/auth/password.py">update</a>(\*\*<a href="src/storyden/types/auth/password_update_params.py">params</a>) -> <a href="./src/storyden/types/auth/password_update_response.py">PasswordUpdateResponse</a></code>
- <code title="post /v1/auth/password/signin">client.auth.password.<a href="./src/storyden/resources/auth/password.py">signin</a>(\*\*<a href="src/storyden/types/auth/password_signin_params.py">params</a>) -> <a href="./src/storyden/types/auth/password_signin_response.py">PasswordSigninResponse</a></code>

## OAuthCallback

Types:

```python
from storyden.types.auth import OAuthCallbackCreateResponse
```

Methods:

- <code title="post /v1/auth/oauth/{oauth_provider}/callback">client.auth.oauth_callback.<a href="./src/storyden/resources/auth/oauth_callback.py">create</a>(oauth_provider, \*\*<a href="src/storyden/types/auth/oauth_callback_create_params.py">params</a>) -> <a href="./src/storyden/types/auth/oauth_callback_create_response.py">OAuthCallbackCreateResponse</a></code>

## Webauthn

### Make

Types:

```python
from storyden.types.auth.webauthn import MakeCreateResponse, MakeRetrieveResponse
```

Methods:

- <code title="post /v1/auth/webauthn/make">client.auth.webauthn.make.<a href="./src/storyden/resources/auth/webauthn/make.py">create</a>(\*\*<a href="src/storyden/types/auth/webauthn/make_create_params.py">params</a>) -> <a href="./src/storyden/types/auth/webauthn/make_create_response.py">MakeCreateResponse</a></code>
- <code title="get /v1/auth/webauthn/make/{account_handle}">client.auth.webauthn.make.<a href="./src/storyden/resources/auth/webauthn/make.py">retrieve</a>(account_handle) -> <a href="./src/storyden/types/auth/webauthn/make_retrieve_response.py">MakeRetrieveResponse</a></code>

### Assert

Types:

```python
from storyden.types.auth.webauthn import AssertCreateResponse, AssertRetrieveResponse
```

Methods:

- <code title="post /v1/auth/webauthn/assert">client.auth.webauthn.assert*.<a href="./src/storyden/resources/auth/webauthn/assert*.py">create</a>(\*\*<a href="src/storyden/types/auth/webauthn/assert_create_params.py">params</a>) -> <a href="./src/storyden/types/auth/webauthn/assert_create_response.py">AssertCreateResponse</a></code>
- <code title="get /v1/auth/webauthn/assert/{account_handle}">client.auth.webauthn.assert*.<a href="./src/storyden/resources/auth/webauthn/assert*.py">retrieve</a>(account_handle) -> <a href="./src/storyden/types/auth/webauthn/assert_retrieve_response.py">AssertRetrieveResponse</a></code>

## Phone

Types:

```python
from storyden.types.auth import PhoneCreateResponse, PhoneUpdateResponse
```

Methods:

- <code title="post /v1/auth/phone">client.auth.phone.<a href="./src/storyden/resources/auth/phone.py">create</a>(\*\*<a href="src/storyden/types/auth/phone_create_params.py">params</a>) -> <a href="./src/storyden/types/auth/phone_create_response.py">PhoneCreateResponse</a></code>
- <code title="put /v1/auth/phone/{account_handle}">client.auth.phone.<a href="./src/storyden/resources/auth/phone.py">update</a>(account_handle, \*\*<a href="src/storyden/types/auth/phone_update_params.py">params</a>) -> <a href="./src/storyden/types/auth/phone_update_response.py">PhoneUpdateResponse</a></code>

# Categories

Types:

```python
from storyden.types import CategoryUpdateResponse, CategoryListResponse, CategoryUpdateOrderResponse
```

Methods:

- <code title="patch /v1/categories/{category_id}">client.categories.<a href="./src/storyden/resources/categories.py">update</a>(category_id, \*\*<a href="src/storyden/types/category_update_params.py">params</a>) -> <a href="./src/storyden/types/category_update_response.py">CategoryUpdateResponse</a></code>
- <code title="get /v1/categories">client.categories.<a href="./src/storyden/resources/categories.py">list</a>() -> <a href="./src/storyden/types/category_list_response.py">CategoryListResponse</a></code>
- <code title="patch /v1/categories">client.categories.<a href="./src/storyden/resources/categories.py">update_order</a>(\*\*<a href="src/storyden/types/category_update_order_params.py">params</a>) -> <a href="./src/storyden/types/category_update_order_response.py">CategoryUpdateOrderResponse</a></code>

# Threads

Types:

```python
from storyden.types import (
    ThreadCreateResponse,
    ThreadListResponse,
    ThreadPublishChangesResponse,
    ThreadRetrieveInformationResponse,
)
```

Methods:

- <code title="post /v1/threads">client.threads.<a href="./src/storyden/resources/threads/threads.py">create</a>(\*\*<a href="src/storyden/types/thread_create_params.py">params</a>) -> <a href="./src/storyden/types/thread_create_response.py">ThreadCreateResponse</a></code>
- <code title="get /v1/threads">client.threads.<a href="./src/storyden/resources/threads/threads.py">list</a>(\*\*<a href="src/storyden/types/thread_list_params.py">params</a>) -> <a href="./src/storyden/types/thread_list_response.py">ThreadListResponse</a></code>
- <code title="delete /v1/threads/{thread_mark}">client.threads.<a href="./src/storyden/resources/threads/threads.py">archive</a>(thread_mark) -> None</code>
- <code title="patch /v1/threads/{thread_mark}">client.threads.<a href="./src/storyden/resources/threads/threads.py">publish_changes</a>(thread_mark, \*\*<a href="src/storyden/types/thread_publish_changes_params.py">params</a>) -> <a href="./src/storyden/types/thread_publish_changes_response.py">ThreadPublishChangesResponse</a></code>
- <code title="get /v1/threads/{thread_mark}">client.threads.<a href="./src/storyden/resources/threads/threads.py">retrieve_information</a>(thread_mark) -> <a href="./src/storyden/types/thread_retrieve_information_response.py">ThreadRetrieveInformationResponse</a></code>

## Posts

Types:

```python
from storyden.types.threads import PostCreateResponse
```

Methods:

- <code title="post /v1/threads/{thread_mark}/posts">client.threads.posts.<a href="./src/storyden/resources/threads/posts.py">create</a>(thread_mark, \*\*<a href="src/storyden/types/threads/post_create_params.py">params</a>) -> <a href="./src/storyden/types/threads/post_create_response.py">PostCreateResponse</a></code>

# Posts

Types:

```python
from storyden.types import PostUpdateResponse, PostReactsResponse, PostSearchResponse
```

Methods:

- <code title="patch /v1/posts/{post_id}">client.posts.<a href="./src/storyden/resources/posts.py">update</a>(post_id, \*\*<a href="src/storyden/types/post_update_params.py">params</a>) -> <a href="./src/storyden/types/post_update_response.py">PostUpdateResponse</a></code>
- <code title="delete /v1/posts/{post_id}">client.posts.<a href="./src/storyden/resources/posts.py">archive</a>(post_id) -> None</code>
- <code title="put /v1/posts/{post_id}/reacts">client.posts.<a href="./src/storyden/resources/posts.py">reacts</a>(post_id, \*\*<a href="src/storyden/types/post_reacts_params.py">params</a>) -> <a href="./src/storyden/types/post_reacts_response.py">PostReactsResponse</a></code>
- <code title="get /v1/posts/search">client.posts.<a href="./src/storyden/resources/posts.py">search</a>(\*\*<a href="src/storyden/types/post_search_params.py">params</a>) -> <a href="./src/storyden/types/post_search_response.py">PostSearchResponse</a></code>

# Assets

Types:

```python
from storyden.types import AssetCreateResponse
```

Methods:

- <code title="post /v1/assets">client.assets.<a href="./src/storyden/resources/assets.py">create</a>(\*\*<a href="src/storyden/types/asset_create_params.py">params</a>) -> <a href="./src/storyden/types/asset_create_response.py">AssetCreateResponse</a></code>
- <code title="get /v1/assets/{asset_filename}">client.assets.<a href="./src/storyden/resources/assets.py">retrieve</a>(asset_filename) -> BinaryAPIResponse</code>

# Collections

Types:

```python
from storyden.types import (
    CollectionCreateResponse,
    CollectionRetrieveResponse,
    CollectionUpdateResponse,
    CollectionListResponse,
)
```

Methods:

- <code title="post /v1/collections">client.collections.<a href="./src/storyden/resources/collections/collections.py">create</a>(\*\*<a href="src/storyden/types/collection_create_params.py">params</a>) -> <a href="./src/storyden/types/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="get /v1/collections/{collection_id}">client.collections.<a href="./src/storyden/resources/collections/collections.py">retrieve</a>(collection_id) -> <a href="./src/storyden/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>
- <code title="patch /v1/collections/{collection_id}">client.collections.<a href="./src/storyden/resources/collections/collections.py">update</a>(collection_id, \*\*<a href="src/storyden/types/collection_update_params.py">params</a>) -> <a href="./src/storyden/types/collection_update_response.py">CollectionUpdateResponse</a></code>
- <code title="get /v1/collections">client.collections.<a href="./src/storyden/resources/collections/collections.py">list</a>(\*\*<a href="src/storyden/types/collection_list_params.py">params</a>) -> <a href="./src/storyden/types/collection_list_response.py">CollectionListResponse</a></code>

# Links

Types:

```python
from storyden.types import LinkCreateResponse, LinkRetrieveResponse, LinkListResponse
```

Methods:

- <code title="post /v1/links">client.links.<a href="./src/storyden/resources/links.py">create</a>(\*\*<a href="src/storyden/types/link_create_params.py">params</a>) -> <a href="./src/storyden/types/link_create_response.py">LinkCreateResponse</a></code>
- <code title="get /v1/links/{link_slug}">client.links.<a href="./src/storyden/resources/links.py">retrieve</a>(link_slug) -> <a href="./src/storyden/types/link_retrieve_response.py">LinkRetrieveResponse</a></code>
- <code title="get /v1/links">client.links.<a href="./src/storyden/resources/links.py">list</a>(\*\*<a href="src/storyden/types/link_list_params.py">params</a>) -> <a href="./src/storyden/types/link_list_response.py">LinkListResponse</a></code>

# Datagraph

Types:

```python
from storyden.types import DatagraphListResponse
```

Methods:

- <code title="get /v1/datagraph">client.datagraph.<a href="./src/storyden/resources/datagraph.py">list</a>(\*\*<a href="src/storyden/types/datagraph_list_params.py">params</a>) -> <a href="./src/storyden/types/datagraph_list_response.py">DatagraphListResponse</a></code>
