const crypto = require('crypto')

function m(e) {
    return crypto.createHash("md5").update(e).digest()
}

function decode(t, o, n) {
    if (!t)
        return null;
    const a = Buffer.alloc(16, m(o))
        , i = Buffer.alloc(16, m(n))
        , r = crypto.createDecipheriv("aes-128-cbc", a, i);
    let s = r.update(t, "base64", "utf-8");
    return s += r.final("utf-8"),
        s
}

var key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
var iiv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

function run(o) {
    return (decode(o, key, iiv))
}
