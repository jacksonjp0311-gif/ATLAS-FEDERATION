# Investigation 36 — Valid hash but denied community release

An author-created test blob has a known SHA-256 digest. A metadata packet says the community permission was denied. The local bytes match the expected hash; the release decision is still `do_not_distribute`. This separates data integrity from authority. A second packet says consent is documented, source bytes match and access is public; it remains **eligible for external rights review only**, not automatically publishable.

Such fields are only caller assertions. The program cannot authenticate a speaker, negotiate a cultural authority agreement, or determine lawful reuse. A real archive must have trusted consent records, community governance, withdrawal procedures and access controls. These are essential to preserving language without exploiting knowledge holders.

No actual community data is included.
