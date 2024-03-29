## General

<table><tbody><tr id="//dash_ref_General/Entry/GET request/0"><td colspan="2"><p>GET request</p><div><pre><span>// Make a request for a user with a given ID</span>
<span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user?ID=12345</span><span>'</span><span>)</span>
  <span>.</span><span>then</span><span>(</span><span>function</span> <span>(</span><span>response</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>);</span>
  <span>})</span>
  <span>.</span><span>catch</span><span>(</span><span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>);</span>
  <span>});</span>

<span>// Optionally the request above could also be done as</span>
<span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user</span><span>'</span><span>,</span> <span>{</span>
    <span>params</span><span>:</span> <span>{</span>
      <span>ID</span><span>:</span> <span>12345</span>
    <span>}</span>
  <span>})</span>
  <span>.</span><span>then</span><span>(</span><span>function</span> <span>(</span><span>response</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>);</span>
  <span>})</span>
  <span>.</span><span>catch</span><span>(</span><span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>);</span>
  <span>});</span></pre></div></td></tr><tr id="//dash_ref_General/Entry/POST request/0"><td colspan="2"><p>POST request</p><div><pre><span>axios</span><span>.</span><span>post</span><span>(</span><span>'</span><span>/user</span><span>'</span><span>,</span> <span>{</span>
    <span>firstName</span><span>:</span> <span>'</span><span>Fred</span><span>'</span><span>,</span>
    <span>lastName</span><span>:</span> <span>'</span><span>Flintstone</span><span>'</span>
  <span>})</span>
  <span>.</span><span>then</span><span>(</span><span>function</span> <span>(</span><span>response</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>);</span>
  <span>})</span>
  <span>.</span><span>catch</span><span>(</span><span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>);</span>
  <span>});</span></pre></div></td></tr><tr id="//dash_ref_General/Entry/Multiple concurrent requests/0"><td colspan="2"><p>Multiple concurrent requests</p><div><pre><span>function</span> <span>getUserAccount</span><span>()</span> <span>{</span>
  <span>return</span> <span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>);</span>
<span>}</span>

<span>function</span> <span>getUserPermissions</span><span>()</span> <span>{</span>
  <span>return</span> <span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345/permissions</span><span>'</span><span>);</span>
<span>}</span>

<span>axios</span><span>.</span><span>all</span><span>([</span><span>getUserAccount</span><span>(),</span> <span>getUserPermissions</span><span>()])</span>
  <span>.</span><span>then</span><span>(</span><span>axios</span><span>.</span><span>spread</span><span>(</span><span>function</span> <span>(</span><span>acct</span><span>,</span> <span>perms</span><span>)</span> <span>{</span>
    <span>// Both requests are now complete</span>
  <span>}));</span></pre></div></td></tr><tr id="//dash_ref_General/Entry/POST request config/0"><td colspan="2"><p>POST request config</p><div><pre><span>// Send a POST request</span>
<span>axios</span><span>({</span>
  <span>method</span><span>:</span> <span>'</span><span>post</span><span>'</span><span>,</span>
  <span>url</span><span>:</span> <span>'</span><span>/user/12345</span><span>'</span><span>,</span>
  <span>data</span><span>:</span> <span>{</span>
    <span>firstName</span><span>:</span> <span>'</span><span>Fred</span><span>'</span><span>,</span>
    <span>lastName</span><span>:</span> <span>'</span><span>Flintstone</span><span>'</span>
  <span>}</span>
<span>});</span></pre></div></td></tr><tr id="//dash_ref_General/Entry/GET request config/0"><td colspan="2"><p>GET request config</p><div><pre><span>// GET request for remote image</span>
<span>axios</span><span>({</span>
  <span>method</span><span>:</span> <span>'</span><span>get</span><span>'</span><span>,</span>
  <span>url</span><span>:</span> <span>'</span><span>http://bit.ly/2mTM3nY</span><span>'</span><span>,</span>
  <span>responseType</span><span>:</span> <span>'</span><span>stream</span><span>'</span>
<span>})</span>
  <span>.</span><span>then</span><span>(</span><span>function</span><span>(</span><span>response</span><span>)</span> <span>{</span>
  <span>response</span><span>.</span><span>data</span><span>.</span><span>pipe</span><span>(</span><span>fs</span><span>.</span><span>createWriteStream</span><span>(</span><span>'</span><span>ada_lovelace.jpg</span><span>'</span><span>))</span>
<span>});</span></pre></div></td></tr><tr id="//dash_ref_General/Entry/Create instance/0"><td colspan="2"><p>Create instance</p><div><pre><span>var</span> <span>instance</span> <span>=</span> <span>axios</span><span>.</span><span>create</span><span>({</span>
  <span>baseURL</span><span>:</span> <span>'</span><span>https://some-domain.com/api/</span><span>'</span><span>,</span>
  <span>timeout</span><span>:</span> <span>1000</span><span>,</span>
  <span>headers</span><span>:</span> <span>{</span><span>'</span><span>X-Custom-Header</span><span>'</span><span>:</span> <span>'</span><span>foobar</span><span>'</span><span>}</span>
<span>});</span></pre></div></td></tr></tbody></table>

## API

<table><tbody><tr id="//dash_ref_API/Entry/Request method aliases/0"><td colspan="2"><p>Request method aliases</p><p></p><h5>axios.request(config)</h5><h5>axios.get(url[, config])</h5><h5>axios.delete(url[, config])</h5><h5>axios.head(url[, config])</h5><h5>axios.options(url[, config])</h5><h5>axios.post(url[, data[, config]])</h5><h5>axios.put(url[, data[, config]])</h5><h5>axios.patch(url[, data[, config]])</h5><p></p></td></tr><tr id="//dash_ref_API/Entry/Concurrency/0"><td colspan="2"><p>Concurrency</p><p></p><h5>axios.all(iterable)</h5><h5>axios.spread(callback)</h5><p></p></td></tr><tr id="//dash_ref_API/Entry/Instance methods/0"><td colspan="2"><p>Instance methods</p><p></p><h5>axios#create([config])</h5><h5>axios#request(config)</h5><h5>axios#get(url[, config])</h5><h5>axios#delete(url[, config])</h5><h5>axios#head(url[, config])</h5><h5>axios#options(url[, config])</h5><h5>axios#post(url[, data[, config]])</h5><h5>axios#put(url[, data[, config]])</h5><h5>axios#patch(url[, data[, config]])</h5><p></p></td></tr></tbody></table>

## Request Config

Request options

```
<span>{</span>
  <span>// `url` is the server URL that will be used for the request</span>
  <span>url</span><span>:</span> <span>'</span><span>/user</span><span>'</span><span>,</span>

  <span>// `method` is the request method to be used when making the request</span>
  <span>method</span><span>:</span> <span>'</span><span>get</span><span>'</span><span>,</span> <span>// default</span>

  <span>// `baseURL` will be prepended to `url` unless `url` is absolute.</span>
  <span>// It can be convenient to set `baseURL` for an instance of axios to pass relative URLs</span>
  <span>// to methods of that instance.</span>
  <span>baseURL</span><span>:</span> <span>'</span><span>https://some-domain.com/api/</span><span>'</span><span>,</span>

  <span>// `transformRequest` allows changes to the request data before it is sent to the server</span>
  <span>// This is only applicable for request methods 'PUT', 'POST', and 'PATCH'</span>
  <span>// The last function in the array must return a string or an instance of Buffer, ArrayBuffer,</span>
  <span>// FormData or Stream</span>
  <span>// You may modify the headers object.</span>
  <span>transformRequest</span><span>:</span> <span>[</span><span>function</span> <span>(</span><span>data</span><span>,</span> <span>headers</span><span>)</span> <span>{</span>
    <span>// Do whatever you want to transform the data</span>

    <span>return</span> <span>data</span><span>;</span>
  <span>}],</span>

  <span>// `transformResponse` allows changes to the response data to be made before</span>
  <span>// it is passed to then/catch</span>
  <span>transformResponse</span><span>:</span> <span>[</span><span>function</span> <span>(</span><span>data</span><span>)</span> <span>{</span>
    <span>// Do whatever you want to transform the data</span>

    <span>return</span> <span>data</span><span>;</span>
  <span>}],</span>

  <span>// `headers` are custom headers to be sent</span>
  <span>headers</span><span>:</span> <span>{</span><span>'</span><span>X-Requested-With</span><span>'</span><span>:</span> <span>'</span><span>XMLHttpRequest</span><span>'</span><span>},</span>

  <span>// `params` are the URL parameters to be sent with the request</span>
  <span>// Must be a plain object or a URLSearchParams object</span>
  <span>params</span><span>:</span> <span>{</span>
    <span>ID</span><span>:</span> <span>12345</span>
  <span>},</span>

  <span>// `paramsSerializer` is an optional function in charge of serializing `params`</span>
  <span>// (e.g. https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)</span>
  <span>paramsSerializer</span><span>:</span> <span>function</span><span>(</span><span>params</span><span>)</span> <span>{</span>
    <span>return</span> <span>Qs</span><span>.</span><span>stringify</span><span>(</span><span>params</span><span>,</span> <span>{</span><span>arrayFormat</span><span>:</span> <span>'</span><span>brackets</span><span>'</span><span>})</span>
  <span>},</span>

  <span>// `data` is the data to be sent as the request body</span>
  <span>// Only applicable for request methods 'PUT', 'POST', and 'PATCH'</span>
  <span>// When no `transformRequest` is set, must be of one of the following types:</span>
  <span>// - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams</span>
  <span>// - Browser only: FormData, File, Blob</span>
  <span>// - Node only: Stream, Buffer</span>
  <span>data</span><span>:</span> <span>{</span>
    <span>firstName</span><span>:</span> <span>'</span><span>Fred</span><span>'</span>
  <span>},</span>

  <span>// `timeout` specifies the number of milliseconds before the request times out.</span>
  <span>// If the request takes longer than `timeout`, the request will be aborted.</span>
  <span>timeout</span><span>:</span> <span>1000</span><span>,</span>

  <span>// `withCredentials` indicates whether or not cross-site Access-Control requests</span>
  <span>// should be made using credentials</span>
  <span>withCredentials</span><span>:</span> <span>false</span><span>,</span> <span>// default</span>

  <span>// `adapter` allows custom handling of requests which makes testing easier.</span>
  <span>// Return a promise and supply a valid response (see lib/adapters/README.md).</span>
  <span>adapter</span><span>:</span> <span>function</span> <span>(</span><span>config</span><span>)</span> <span>{</span>
    <span>/* ... */</span>
  <span>},</span>

  <span>// `auth` indicates that HTTP Basic auth should be used, and supplies credentials.</span>
  <span>// This will set an `Authorization` header, overwriting any existing</span>
  <span>// `Authorization` custom headers you have set using `headers`.</span>
  <span>auth</span><span>:</span> <span>{</span>
    <span>username</span><span>:</span> <span>'</span><span>janedoe</span><span>'</span><span>,</span>
    <span>password</span><span>:</span> <span>'</span><span>s00pers3cret</span><span>'</span>
  <span>},</span>

  <span>// `responseType` indicates the type of data that the server will respond with</span>
  <span>// options are 'arraybuffer', 'blob', 'document', 'json', 'text', 'stream'</span>
  <span>responseType</span><span>:</span> <span>'</span><span>json</span><span>'</span><span>,</span> <span>// default</span>

  <span>// `xsrfCookieName` is the name of the cookie to use as a value for xsrf token</span>
  <span>xsrfCookieName</span><span>:</span> <span>'</span><span>XSRF-TOKEN</span><span>'</span><span>,</span> <span>// default</span>

  <span>// `xsrfHeaderName` is the name of the http header that carries the xsrf token value</span>
  <span>xsrfHeaderName</span><span>:</span> <span>'</span><span>X-XSRF-TOKEN</span><span>'</span><span>,</span> <span>// default</span>

  <span>// `onUploadProgress` allows handling of progress events for uploads</span>
  <span>onUploadProgress</span><span>:</span> <span>function</span> <span>(</span><span>progressEvent</span><span>)</span> <span>{</span>
    <span>// Do whatever you want with the native progress event</span>
  <span>},</span>

  <span>// `onDownloadProgress` allows handling of progress events for downloads</span>
  <span>onDownloadProgress</span><span>:</span> <span>function</span> <span>(</span><span>progressEvent</span><span>)</span> <span>{</span>
    <span>// Do whatever you want with the native progress event</span>
  <span>},</span>

  <span>// `maxContentLength` defines the max size of the http response content allowed</span>
  <span>maxContentLength</span><span>:</span> <span>2000</span><span>,</span>

  <span>// `validateStatus` defines whether to resolve or reject the promise for a given</span>
  <span>// HTTP response status code. If `validateStatus` returns `true` (or is set to `null`</span>
  <span>// or `undefined`), the promise will be resolved; otherwise, the promise will be</span>
  <span>// rejected.</span>
  <span>validateStatus</span><span>:</span> <span>function</span> <span>(</span><span>status</span><span>)</span> <span>{</span>
    <span>return</span> <span>status</span> <span>&gt;=</span> <span>200</span> <span>&amp;&amp;</span> <span>status</span> <span>&lt;</span> <span>300</span><span>;</span> <span>// default</span>
  <span>},</span>

  <span>// `maxRedirects` defines the maximum number of redirects to follow in node.js.</span>
  <span>// If set to 0, no redirects will be followed.</span>
  <span>maxRedirects</span><span>:</span> <span>5</span><span>,</span> <span>// default</span>

  <span>// `httpAgent` and `httpsAgent` define a custom agent to be used when performing http</span>
  <span>// and https requests, respectively, in node.js. This allows options to be added like</span>
  <span>// `keepAlive` that are not enabled by default.</span>
  <span>httpAgent</span><span>:</span> <span>new</span> <span>http</span><span>.</span><span>Agent</span><span>({</span> <span>keepAlive</span><span>:</span> <span>true</span> <span>}),</span>
  <span>httpsAgent</span><span>:</span> <span>new</span> <span>https</span><span>.</span><span>Agent</span><span>({</span> <span>keepAlive</span><span>:</span> <span>true</span> <span>}),</span>

  <span>// 'proxy' defines the hostname and port of the proxy server</span>
  <span>// Use `false` to disable proxies, ignoring environment variables.</span>
  <span>// `auth` indicates that HTTP Basic auth should be used to connect to the proxy, and</span>
  <span>// supplies credentials.</span>
  <span>// This will set an `Proxy-Authorization` header, overwriting any existing</span>
  <span>// `Proxy-Authorization` custom headers you have set using `headers`.</span>
  <span>proxy</span><span>:</span> <span>{</span>
    <span>host</span><span>:</span> <span>'</span><span>127.0.0.1</span><span>'</span><span>,</span>
    <span>port</span><span>:</span> <span>9000</span><span>,</span>
    <span>auth</span><span>:</span> <span>{</span>
      <span>username</span><span>:</span> <span>'</span><span>mikeymike</span><span>'</span><span>,</span>
      <span>password</span><span>:</span> <span>'</span><span>rapunz3l</span><span>'</span>
    <span>}</span>
  <span>},</span>

  <span>// `cancelToken` specifies a cancel token that can be used to cancel the request</span>
  <span>// (see Cancellation section below for details)</span>
  <span>cancelToken</span><span>:</span> <span>new</span> <span>CancelToken</span><span>(</span><span>function</span> <span>(</span><span>cancel</span><span>)</span> <span>{</span>
  <span>})</span>
<span>}</span>
```

## Response Schema

<table><tbody><tr id="//dash_ref_Response Schema/Entry/Request response/0"><td colspan="2"><p>Request response</p><div><pre><span>{</span>
  <span>// `data` is the response that was provided by the server</span>
  <span>data</span><span>:</span> <span>{},</span>

  <span>// `status` is the HTTP status code from the server response</span>
  <span>status</span><span>:</span> <span>200</span><span>,</span>

  <span>// `statusText` is the HTTP status message from the server response</span>
  <span>statusText</span><span>:</span> <span>'</span><span>OK</span><span>'</span><span>,</span>

  <span>// `headers` the headers that the server responded with</span>
  <span>// All header names are lower cased</span>
  <span>headers</span><span>:</span> <span>{},</span>

  <span>// `config` is the config that was provided to `axios` for the request</span>
  <span>config</span><span>:</span> <span>{},</span>

  <span>// `request` is the request that generated this response</span>
  <span>// It is the last ClientRequest instance in node.js (in redirects)</span>
  <span>// and an XMLHttpRequest instance the browser</span>
  <span>request</span><span>:</span> <span>{}</span>
<span>}</span></pre></div></td></tr><tr id="//dash_ref_Response Schema/Entry/Response using then/0"><td colspan="2"><p>Response using <code>then</code></p><div><pre><span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>)</span>
  <span>.</span><span>then</span><span>(</span><span>function</span><span>(</span><span>response</span><span>)</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>.</span><span>data</span><span>);</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>.</span><span>status</span><span>);</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>.</span><span>statusText</span><span>);</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>.</span><span>headers</span><span>);</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>response</span><span>.</span><span>config</span><span>);</span>
  <span>});</span></pre></div></td></tr></tbody></table>

## Config Defaults

<table><tbody><tr id="//dash_ref_Config Defaults/Entry/Global axios defaults/0"><td colspan="2"><p>Global axios defaults</p><div><pre><span>axios</span><span>.</span><span>defaults</span><span>.</span><span>baseURL</span> <span>=</span> <span>'</span><span>https://api.example.com</span><span>'</span><span>;</span>
<span>axios</span><span>.</span><span>defaults</span><span>.</span><span>headers</span><span>.</span><span>common</span><span>[</span><span>'</span><span>Authorization</span><span>'</span><span>]</span> <span>=</span> <span>AUTH_TOKEN</span><span>;</span>
<span>axios</span><span>.</span><span>defaults</span><span>.</span><span>headers</span><span>.</span><span>post</span><span>[</span><span>'</span><span>Content-Type</span><span>'</span><span>]</span> <span>=</span> <span>'</span><span>application/x-www-form-urlencoded</span><span>'</span><span>;</span></pre></div></td></tr><tr id="//dash_ref_Config Defaults/Entry/Custom instance defaults/0"><td colspan="2"><p>Custom instance defaults</p><div><pre><span>// Set config defaults when creating the instance</span>
<span>var</span> <span>instance</span> <span>=</span> <span>axios</span><span>.</span><span>create</span><span>({</span>
  <span>baseURL</span><span>:</span> <span>'</span><span>https://api.example.com</span><span>'</span>
<span>});</span>

<span>// Alter defaults after instance has been created</span>
<span>instance</span><span>.</span><span>defaults</span><span>.</span><span>headers</span><span>.</span><span>common</span><span>[</span><span>'</span><span>Authorization</span><span>'</span><span>]</span> <span>=</span> <span>AUTH_TOKEN</span><span>;</span></pre></div></td></tr><tr id="//dash_ref_Config Defaults/Entry/Config order of precedence/0"><td colspan="2"><p>Config order of precedence</p><div><pre><span>// Create an instance using the config defaults provided by the library</span>
<span>// At this point the timeout config value is `0` as is the default for the library</span>
<span>var</span> <span>instance</span> <span>=</span> <span>axios</span><span>.</span><span>create</span><span>();</span>

<span>// Override timeout default for the library</span>
<span>// Now all requests will wait 2.5 seconds before timing out</span>
<span>instance</span><span>.</span><span>defaults</span><span>.</span><span>timeout</span> <span>=</span> <span>2500</span><span>;</span>

<span>// Override timeout for this request as it's known to take a long time</span>
<span>instance</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/longRequest</span><span>'</span><span>,</span> <span>{</span>
  <span>timeout</span><span>:</span> <span>5000</span>
<span>});</span></pre></div></td></tr></tbody></table>

## Interceptors

<table><tbody><tr id="//dash_ref_Interceptors/Entry/Intercept request%2Fresponses/0"><td colspan="2"><p>Intercept request/responses</p><div><pre><span>// Add a request interceptor</span>
<span>axios</span><span>.</span><span>interceptors</span><span>.</span><span>request</span><span>.</span><span>use</span><span>(</span><span>function</span> <span>(</span><span>config</span><span>)</span> <span>{</span>
    <span>// Do something before request is sent</span>
    <span>return</span> <span>config</span><span>;</span>
  <span>},</span> <span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>// Do something with request error</span>
    <span>return</span> <span>Promise</span><span>.</span><span>reject</span><span>(</span><span>error</span><span>);</span>
  <span>});</span>

<span>// Add a response interceptor</span>
<span>axios</span><span>.</span><span>interceptors</span><span>.</span><span>response</span><span>.</span><span>use</span><span>(</span><span>function</span> <span>(</span><span>response</span><span>)</span> <span>{</span>
    <span>// Do something with response data</span>
    <span>return</span> <span>response</span><span>;</span>
  <span>},</span> <span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>// Do something with response error</span>
    <span>return</span> <span>Promise</span><span>.</span><span>reject</span><span>(</span><span>error</span><span>);</span>
  <span>});</span></pre></div></td></tr><tr id="//dash_ref_Interceptors/Entry/Remove interceptor/0"><td colspan="2"><p>Remove interceptor</p><div><pre><span>var</span> <span>myInterceptor</span> <span>=</span> <span>axios</span><span>.</span><span>interceptors</span><span>.</span><span>request</span><span>.</span><span>use</span><span>(</span><span>function</span> <span>()</span> <span>{</span><span>/*...*/</span><span>});</span>
<span>axios</span><span>.</span><span>interceptors</span><span>.</span><span>request</span><span>.</span><span>eject</span><span>(</span><span>myInterceptor</span><span>);</span></pre></div></td></tr><tr id="//dash_ref_Interceptors/Entry/Custom instance interceptors/0"><td colspan="2"><p>Custom instance interceptors</p><div><pre><span>var</span> <span>instance</span> <span>=</span> <span>axios</span><span>.</span><span>create</span><span>();</span>
<span>instance</span><span>.</span><span>interceptors</span><span>.</span><span>request</span><span>.</span><span>use</span><span>(</span><span>function</span> <span>()</span> <span>{</span><span>/*...*/</span><span>});</span></pre></div></td></tr></tbody></table>

## Handling Errors

<table><tbody><tr id="//dash_ref_Handling Errors/Entry/Catch error/0"><td colspan="2"><p>Catch error</p><div><pre><span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>)</span>
  <span>.</span><span>catch</span><span>(</span><span>function</span> <span>(</span><span>error</span><span>)</span> <span>{</span>
    <span>if</span> <span>(</span><span>error</span><span>.</span><span>response</span><span>)</span> <span>{</span>
      <span>// The request was made and the server responded with a status code</span>
      <span>// that falls out of the range of 2xx</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>.</span><span>response</span><span>.</span><span>data</span><span>);</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>.</span><span>response</span><span>.</span><span>status</span><span>);</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>.</span><span>response</span><span>.</span><span>headers</span><span>);</span>
    <span>}</span> <span>else</span> <span>if</span> <span>(</span><span>error</span><span>.</span><span>request</span><span>)</span> <span>{</span>
      <span>// The request was made but no response was received</span>
      <span>// `error.request` is an instance of XMLHttpRequest in the browser and an instance of</span>
      <span>// http.ClientRequest in node.js</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>.</span><span>request</span><span>);</span>
    <span>}</span> <span>else</span> <span>{</span>
      <span>// Something happened in setting up the request that triggered an Error</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>'</span><span>Error</span><span>'</span><span>,</span> <span>error</span><span>.</span><span>message</span><span>);</span>
    <span>}</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>error</span><span>.</span><span>config</span><span>);</span>
  <span>});</span></pre></div></td></tr><tr id="//dash_ref_Handling Errors/Entry/Custom HTTP status code error/0"><td colspan="2"><p>Custom HTTP status code error</p><div><pre><span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>,</span> <span>{</span>
  <span>validateStatus</span><span>:</span> <span>function</span> <span>(</span><span>status</span><span>)</span> <span>{</span>
    <span>return</span> <span>status</span> <span>&lt;</span> <span>500</span><span>;</span> <span>// Reject only if the status code is greater than or equal to 500</span>
  <span>}</span>
<span>})</span></pre></div></td></tr></tbody></table>

## Cancellation

<table><tbody><tr id="//dash_ref_Cancellation/Entry/Cancel request with cancel token/0"><td colspan="2"><p>Cancel request with cancel token</p><div><pre><span>var</span> <span>CancelToken</span> <span>=</span> <span>axios</span><span>.</span><span>CancelToken</span><span>;</span>
<span>var</span> <span>source</span> <span>=</span> <span>CancelToken</span><span>.</span><span>source</span><span>();</span>

<span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>,</span> <span>{</span>
  <span>cancelToken</span><span>:</span> <span>source</span><span>.</span><span>token</span>
<span>}).</span><span>catch</span><span>(</span><span>function</span><span>(</span><span>thrown</span><span>)</span> <span>{</span>
  <span>if</span> <span>(</span><span>axios</span><span>.</span><span>isCancel</span><span>(</span><span>thrown</span><span>))</span> <span>{</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>'</span><span>Request canceled</span><span>'</span><span>,</span> <span>thrown</span><span>.</span><span>message</span><span>);</span>
  <span>}</span> <span>else</span> <span>{</span>
    <span>// handle error</span>
  <span>}</span>
<span>});</span>

<span>axios</span><span>.</span><span>post</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>,</span> <span>{</span>
  <span>name</span><span>:</span> <span>'</span><span>new name</span><span>'</span>
<span>},</span> <span>{</span>
  <span>cancelToken</span><span>:</span> <span>source</span><span>.</span><span>token</span>
<span>})</span>

<span>// cancel the request (the message parameter is optional)</span>
<span>source</span><span>.</span><span>cancel</span><span>(</span><span>'</span><span>Operation canceled by the user.</span><span>'</span><span>);</span></pre></div></td></tr><tr id="//dash_ref_Cancellation/Entry/Create cancel token/0"><td colspan="2"><p>Create cancel token</p><div><pre><span>var</span> <span>CancelToken</span> <span>=</span> <span>axios</span><span>.</span><span>CancelToken</span><span>;</span>
<span>var</span> <span>cancel</span><span>;</span>

<span>axios</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/user/12345</span><span>'</span><span>,</span> <span>{</span>
  <span>cancelToken</span><span>:</span> <span>new</span> <span>CancelToken</span><span>(</span><span>function</span> <span>executor</span><span>(</span><span>c</span><span>)</span> <span>{</span>
    <span>// An executor function receives a cancel function as a parameter</span>
    <span>cancel</span> <span>=</span> <span>c</span><span>;</span>
  <span>})</span>
<span>});</span>

<span>// cancel the request</span>
<span>cancel</span><span>();</span></pre></div></td></tr></tbody></table>