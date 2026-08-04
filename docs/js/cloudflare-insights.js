// Cloudflare Web Analytics beacon — cookie-less, privacy-friendly, no consent banner required.
// Replace YOUR_BEACON_TOKEN_HERE with the real token from the Cloudflare dashboard
// (Website → Analytics → Web Analytics → enable for the zone → copy beacon token).
// Until the token is replaced, the script returns 404 and analytics are silently disabled.
(function() {
  var script = document.createElement('script');
  script.defer = true;
  script.src = 'https://static.cloudflareinsights.com/beacon.min.js';
  script.setAttribute('data-cf-beacon', '{"token": "YOUR_BEACON_TOKEN_HERE"}');
  document.head.appendChild(script);
})();
