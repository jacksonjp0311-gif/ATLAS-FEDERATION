# 47. Signed languages require simultaneous, not merely sequential, representation

Signed languages are natural languages with multiple interacting articulatory channels. Manual movement, handshape, location, orientation, facial expression, torso and gaze can contribute linguistic structure. A transcript rendered as one line of English glosses loses simultaneity, spatial relationships and many grammatical features. Automatic text-only transformation cannot be assumed to preserve their meaning. The distinction between a gesture and a signed linguistic element is language- and context-dependent and requires expertise and source observation.

## An annotation model

A practical annotation package uses tiers: each tier names one observation channel, time intervals have a declared time base, and annotations include source identity and analysis revision. Two tiers may overlap legitimately; for example, a facial expression can co-occur with a manual sign, and nonmanual markers may span multiple sequential manual events. Even within one tier overlap can reflect alternative analyses, not necessarily a data error.

`multimodal_tier_audit` checks bounded metadata, finite nonnegative start and end times, unique event IDs and reports within-tier overlap without declaring the transcript invalid. It does not process actual video or recognize a sign. A source video that is not stored cannot be reconstructed from a timing table; the Atlas must explicitly mark the missing media. Audio/video, transcript, phonetic descriptions and morphological glosses are distinct layers of evidence.

## Reconstruction requirements

For real language data, preservation would require source recording rights and consent, frame rate and synchronization, named annotation tiers, video quality, filming conditions, community-preferred transcription, gloss vocabulary, analysis disagreements, event IDs and ability to connect the original media to its annotations. None of those materials is acquired here. The toy case has a hands tier from 0–250 ms and a face tier from 100–200 ms; the overlap is allowed and does not demonstrate any particular grammatical meaning.

**Source:** Linguistic Society of America's public signed-language reference, UD/glossing context and ethical documentation references. No authentic signed-language recording or signer evaluation is included.
