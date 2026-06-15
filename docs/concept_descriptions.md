**Class List:** physical, emotional, agentic, enviornmental, syntax, spatial, cognitive, visual, biological

**Concept List:** object, action, qualifier, structural, punctuation, alpha, numeric, alphanumeric, glyph, question, whitesapce, unknown, certainty, absoluteness, polarity, insult, formality, morality, hierarchy, scale, worth, plurality, necessity, temporality, quickness, nothingness, dynamism, continuity, artificiality, agency, abstractness, mysticism, affect, arousal, fear, hedonics, valence, mass, time, length, width, height, temperature, luminance, origin, destination, lateralism, verticality, precedence, dimensionality, containment, boundary, proximity, rotational, terrestrial, gaseousness, fluidity, ignition, safety, shelter, sustenance, gender, audibility, palatability, olfactibility, hue, saturation, color_value, transparency, strength, dexterity, intelligence, wisdom, constitution, 

---  


**Class:** syntax  
**Concept:** object  
**Mapping:** unipolar  

**Description:** Measures the degree to which a token functions as a linguistic entity, person, place, thing, or pronoun. Scales from complete absence of nominal function (0.0) up to a textbook, unambiguous noun or pronoun acting as a core subject or object (4.0). Words with nominalized dual-roles (like gerunds or noun adjuncts) should receive intermediate values.

---

**Class:** syntax  
**Concept:** action  
**Mapping:** unipolar  

**Description:** Measures the degree to which a token denotes a physical action, mental process, or state of being. Maps to verbs, including main, auxiliary, modal, and phrasal verbs. Scales from zero verbal function (0.0) up to an absolute, finite main verb (4.0). Non-finite verb forms like infinitives and participles should scale between 1.5 and 3.0 based on verbal intensity.

---

**Class:** syntax  
**Concept:** qualifier  
**Mapping:** unipolar  

**Description:** Measures the degree to which a token serves to modify, describe, limit, or quantify an object or action. Maps directly to adjectives and adverbs. Scales from non-modifier status (0.0) up to a pure, dedicated descriptive modifier (4.0). Nouns functioning as modifiers or verbs acting as participles should receive intermediate scores.

---

**Class:** syntax  
**Concept:** structural  
**Mapping:** unipolar  

**Description:** Measures the degree to which a token serves a purely grammatical, structure-building, or connective role within a sentence rather than carrying lexical meaning. Maps to prepositions, conjunctions, and determiners (e.g., 'the', 'a', 'in', 'and'). Scales from semantic content words (0.0) up to absolute closed-class function words (4.0).

---

**Class:** syntax  
**Concept:** punctuation  
**Mapping:** unipolar  

**Description:** Measures whether the token represents a standard, grammatically significant punctuation mark used to establish sentence boundaries and structural clauses. Maps to periods, commas, colons, semicolons, dashes, and quotation marks. Scales from standard lexical tokens (0.0) up to explicit, standard grammatical punctuation marks (4.0).

---

**Class:** syntax  
**Concept:** alpha  
**Mapping:** unipolar  

**Description:** Measures the literal composition of the token as an isolated alphabetical character, completely independent of case or semantic meaning. Scales from multi-character sequences or non-alphabetic symbols (0.0) up to a single, standalone character from the a-z or A-Z alphabet (4.0).

---

**Class:** syntax  
**Concept:** numeric  
**Mapping:** unipolar  

**Description:** Measures the presence of literal numeric quantitative information. Maps to raw digits (e.g., '1', '2.5') and explicitly spelled-out cardinal numbers (e.g., 'one', 'hundred'). Scales from zero numeric context (0.0) up to a pure cardinal number token (4.0). Excludes ordinal modifiers like 'first'.

---

**Class:** syntax  
**Concept:** alphanumeric  
**Mapping:** unipolar  

**Description:** Measures whether the token represents a highly structured sequence combining both alphabetic letters and numeric digits. Maps to code identifiers, keys, serial numbers, PINs, or data strings (e.g., 'A123B4') where the blend has specific syntactical significance. Scales from standard words or pure digits (0.0) up to explicit alphanumeric codes (4.0).

---

**Class:** syntax  
**Concept:** glyph  
**Mapping:** unipolar  

**Description:** Measures whether the token represents a non-alphanumeric graphical symbol, icon, special character, or emoji that falls outside standard linguistic punctuation but carries intent (e.g., '@', '#', '&', ':)'). Scales from standard text or standard punctuation (0.0) up to a standalone graphical symbol or non-traditional text glyph (4.0).

---

**Class:** syntax  
**Concept:** question  
**Mapping:** unipolar  

**Description:** Measures the presence of inquisitive or interrogative syntax. Maps to wh-words (e.g., 'who', 'what', 'why'), interrogative auxiliary verbs, or explicit markers used to initiate or formulate questions. Scales from standard declarative language (0.0) up to a dedicated interrogative operator (4.0).

---

**Class:** syntax  
**Concept:** whitesapce  
**Mapping:** unipolar  

**Description:** Measures whether the token functions strictly as a structural, non-printing spatial character used to separate linguistic elements or format text layout. Maps to literal spaces, tabs, line breaks, carriage returns, and mathematical padding tokens. Scales from standard visible alphanumeric text or punctuation (0.0) up to pure, standalone formatting whitespace or layout delimiters (4.0).

---

**Class:** syntax  
**Concept:** unknown  
**Mapping:** unipolar  

**Description:** Measures the degree of lexical or syntactical ambiguity, out-of-vocabulary status, severe spelling errors, or corrupted token strings (e.g., 'whta'). Scales from clean, perfectly identifiable dictionary words (0.0) up to completely un-categorizable, corrupt, or novel linguistic fragments requiring flag or fallback processing (4.0).

---

**Class:** cognitive  
**Concept:** certainty  
**Mapping:** bipolar  

**Description:** Measures epistemic confidence. Negative values represent complete impossibility, random chaos, or total doubt. Zero represents complete ambiguity or a random guess. Positive values represent proven fact, explicit truth, or absolute axiomatic certainty.

---

**Class:** cognitive  
**Concept:** absoluteness  
**Mapping:** unipolar  

**Description:** Measures the degree of totals, absolutes, or boundaries applied to a concept. Scales from loose approximations and partial states up to words denoting totalities, all-encompassing limits, or absolute universal parameters (e.g., some vs. all, part vs. whole).

---

**Class:** cognitive  
**Concept:** polarity  
**Mapping:** bipolar  

**Description:** Measures structural, electrical, or mathematical directionality. Negative values represent systemic deficit, loss, decay, negative, or subtraction. Zero represents static equilibrium, neutral, or stagnation. Positive values represent systemic surplus, growth, creation, positive, or addition.

---

**Class:** cognitive  
**Concept:** insult  
**Mapping:** bipolar  

**Description:** Measures social valence and interpersonal praise. Negative values represent offensive, derogatory expressions, slurs, or deep hostility. Zero represents completely objective, non-evaluative terminology. Positive values represent high praise, compliments, and admiration.

---

**Class:** cognitive  
**Concept:** formality  
**Mapping:** bipolar  

**Description:** Measures socio-linguistic register. Negative values represent highly informal, casual, vulgar, or slang-driven expressions. Zero represents neutral, everyday transactional language. Positive values represent highly academic, formal, ceremonial, or sacred expressions.

---

**Class:** cognitive  
**Concept:** morality  
**Mapping:** bipolar  

**Description:** Measures ethical value. Negative values represent malicious, cruel, or deeply immoral acts. Zero represents ethically neutral physical processes or objective logic. Positive values represent altruistic, just, and exceptionally virtuous principles.

---

**Class:** cognitive  
**Concept:** hierarchy  
**Mapping:** unipolar  

**Description:** The degree of structured rank, priority, position, or stratified authority within a defined social, military, corporate, or ordinal system. Scales from absolute equality up to supreme, unreviewable command.

---

**Class:** cognitive  
**Concept:** scale  
**Mapping:** unipolar  

**Description:** The physical or conceptual size, magnitude, or structural dimension of an object, space, or idea. Scales from microscopic points up to cosmic, universal, or infinite spatial extensions.

---

**Class:** cognitive  
**Concept:** worth  
**Mapping:** bipolar  

**Description:** Measures utility, economic, or functional value. Negative values represent debt, systemic ruin, liabilities, or absolute uselessness. Zero represents completely inert, valueless, or common matter. Positive values represent vital assets, high utility, or priceless, irreplaceable importance.

---

**Class:** cognitive  
**Concept:** plurality  
**Mapping:** unipolar  

**Description:** The grammatical or semantic expression of quantity greater than one. Measures the structural progression from strict singularity up to infinite, massive, or unquantifiable groups of entities.

---

**Class:** cognitive  
**Concept:** necessity  
**Mapping:** bipolar  

**Description:** Measures requirement or systemic demand. Negative values represent forbidden, banned, or explicitly unwanted items. Zero represents optional, trivial, or indifferent items. Positive values represent mandatory, essential, or vital conditions.

---

**Class:** cognitive  
**Concept:** temporality  
**Mapping:** bipolar  

**Description:** Measures temporal direction relative to the observer. Negative values represent the past, historical occurrences, or regression. Zero represents the absolute present moment ('now'). Positive values represent the future, upcoming events, or progression.

---

**Class:** cognitive  
**Concept:** quickness  
**Mapping:** bipolar  

**Description:** Measures rate of movement or execution. Negative values represent sluggish, delayed, or crawling velocity. Zero represents a completely stationary, fixed position. Positive values represent rapid, high-speed, or instantaneous velocity.

---

**Class:** cognitive  
**Concept:** nothingness  
**Mapping:** unipolar  

**Description:** Measures cognitive, mathematical, physical, or philosophical associations with absolute nothingness, voids, empty sets, or zero value. Scales from high-density, fully occupied, or highly significant concepts (0.0) up to terms representing complete depletion, structural vacancies, mathematical zero, or spatial vacuums (4.0) (e.g., 'void', 'empty', 'zero', 'nil', 'vacuum').

---

**Class:** cognitive  
**Concept:** dynamism  
**Mapping:** bipolar  

**Description:** Measures dynamic action versus static posture. Negative values represent rigid, unmoving, frozen, or permanent structural placement. Zero represents transitional or potential energy. Positive values represent high kinetic action, rapid transformation, or vital living activity.

---

**Class:** cognitive  
**Concept:** continuity  
**Mapping:** bipolar  

**Description:** Measures structural flow. Negative values represent fragmented, broken, highly discrete, or atomic steps. Zero represents a paused, frozen, or static state. Positive values represent seamless, unending, smooth, or perpetual fluid motion.

---

**Class:** cognitive  
**Concept:** artificiality  
**Mapping:** bipolar  

**Description:** Measures the origin of structure. Negative values represent pristine, organic, biological, or naturally occurring phenomena. Zero represents transitional states. Positive values represent synthetic, manufactured, technological, or highly engineered artifacts.

---

**Class:** cognitive  
**Concept:** agency  
**Mapping:** unipolar  

**Description:** The degree of intentionality, autonomy, volition, or sentience possessed by an entity. Scales from inert, inanimate physical matter up to self-aware, fully autonomous, or hyper-intelligent beings capable of deliberate action.

---

**Class:** cognitive  
**Concept:** abstractness  
**Mapping:** unipolar  

**Description:** Measures the degree to which a word refers to an intangible idea, cognitive process, or mathematical construct rather than a physical, sensory-accessible object. Scales from literal material items up to pure, un-manifested conceptual frameworks.

---

**Class:** cognitive  
**Concept:** mysticism  
**Mapping:** unipolar  

**Description:** Measures association with supernatural phenomena, esoteric traditions, magical concepts, and historical or superstitious belief systems that bypass material physics. Scales from rigid empirical materialism, mundane reality, or complete secularity (0.0) up to absolute immersion in the unexplained, the paranormal, or deeply entrenched supernatural archetypes (4.0).

---

**Class:** emotional  
**Concept:** affect  
**Mapping:** bipolar  

**Description:** Measures profound relational attachment and sentiment. Negative values represent active loathing, deep malice, or absolute abhorrence. Zero represents absolute apathy or analytical detachment. Positive values represent profound devotion, adoration, or unconditional love.

---

**Class:** emotional  
**Concept:** arousal  
**Mapping:** bipolar  

**Description:** Measures emotional volatility, physiological activation, and agitation. Negative values represent explosive fury, wrath, excitement, or acute hostility. Zero represents a passive, un-aroused, or blank state. Positive values represent profound tranquility, composed stillness, or pacification.

---

**Class:** emotional  
**Concept:** fear  
**Mapping:** unipolar  

**Description:** The cognitive or psychological intensity of distress, terror, or perceived threat associated with a word or situation. Scales from absolute serenity up to paralyzing, catastrophic panic.

---

**Class:** emotional  
**Concept:** hedonics  
**Mapping:** bipolar  

**Description:** Measures immediate physical or psychological sensory feedback. Negative values represent acute pain, visceral discomfort, or deep dissatisfaction. Zero represents a neutral sensory baseline. Positive values represent acute physical comfort, satisfaction, or profound sensory bliss.

---

**Class:** emotional  
**Concept:** valence  
**Mapping:** bipolar  

**Description:** Measures emotional quality regarding sorrow and joy. Negative values represent profound grief, depression, or emotional agony. Zero represents an emotionally flat, clinical, or indifferent state. Positive values represent vibrant joy, elation, or euphoria.

---

**Class:** physical  
**Concept:** mass  
**Mapping:** unipolar  

**Description:** The physical quantitative measurement of matter contained within an object, independent of its size, volume, or dimensions. Scales from weightless/massless phenomena up to ultra-dense or astronomical masses.

---

**Class:** physical  
**Concept:** time  
**Mapping:** unipolar  

**Description:** The expression of temporal duration, interval length, or elapsed periods. Scales from an instantaneous, static moment up to absolute, unceasing eternity.

---

**Class:** physical  
**Concept:** length  
**Mapping:** unipolar  

**Description:** The linear dimension of an object, distance, or spatial measurement along its primary axis. Scales from a zero-dimensional point up to infinite linear distance.

---

**Class:** physical  
**Concept:** width  
**Mapping:** unipolar  

**Description:** The horizontal, lateral, or transverse measurement of an object or space relative to its primary axis. Scales from razor-thin, narrow boundaries up to expansive horizontal spans.

---

**Class:** physical  
**Concept:** height  
**Mapping:** unipolar  

**Description:** The vertical dimension, elevation, or upward extent of an object or position relative to a baseline surface. Scales from completely flat or ground-level states up to the absolute apex of vertical altitude.

---

**Class:** physical  
**Concept:** temperature  
**Mapping:** unipolar  

**Description:** The intensity of thermal energy or kinetic activity of particles within a physical context. Scales from the absence of thermal energy up to extreme, high-energy heat generation.

---

**Class:** physical  
**Concept:** luminance  
**Mapping:** unipolar  

**Description:** The intensity of perceived light, brightness, or visual illumination emitted, reflected, or transmitted by an object or space. Scales from absolute, void-like darkness up to blinding, maximal radiant energy.

---

**Class:** spatial  
**Concept:** origin  
**Mapping:** unipolar  

**Description:** The explicit starting point, causal source, root, or baseline derivation of a path, physical object, historical event, or concept. Scales from an un-originated state up to the absolute primary catalyst or genesis.

---

**Class:** spatial  
**Concept:** destination  
**Mapping:** unipolar  

**Description:** The explicit endpoint, target location, objective, or terminal boundary of a path, trajectory, process, or intention. Scales from directionless drifting up to the absolute finality of arrival.

---

**Class:** spatial  
**Concept:** lateralism  
**Mapping:** bipolar  

**Description:** Measures orientation on the horizontal spatial axis. Negative values indicate leftward direction, western orientation, or port side. Zero represents the exact center or midline. Positive values indicate rightward direction, eastern orientation, or starboard side.

---

**Class:** spatial  
**Concept:** verticality  
**Mapping:** bipolar  

**Description:** Measures orientation on the vertical spatial axis. Negative values indicate downward direction, deep sinking, or a nadir. Zero represents a flat horizontal baseline. Positive values indicate upward direction, climbing, or an apex.

---

**Class:** spatial  
**Concept:** precedence  
**Mapping:** bipolar  

**Description:** Measures orientation along the primary directional axis of travel. Negative values indicate rearward position, physical regression, or backing up. Zero represents a complete standstill. Positive values indicate forward progress, structural advancement, or a vanguard position.

---

**Class:** spatial  
**Concept:** dimensionality  
**Mapping:** unipolar  

**Description:** The geometric complexity or spatial coordinate axes required to define a concept. Scales from a zero-dimensional point (0D) up to higher-dimensional or infinite geometric manifolds.

---

**Class:** spatial  
**Concept:** containment  
**Mapping:** bipolar  

**Description:** Measures spatial encapsulation. Negative values represent being entirely external, outside, or remote from a structure. Zero represents being exactly at the surface, boundary, or skin. Positive values represent being deeply internal, enclosed, or encapsulated within a core.

---

**Class:** spatial  
**Concept:** boundary  
**Mapping:** unipolar  

**Description:** The structural clarity and presence of a limit, perimeter, edge, or barrier dividing spaces or concepts. Scales from boundless, unconstrained space up to an absolute, unpassable, and rigid threshold.

---

**Class:** spatial  
**Concept:** proximity  
**Mapping:** unipolar  

**Description:** The degree of spatial or conceptual closeness between entities. Scales from distant, isolated remoteness up to immediate, adjacent, or overlapping contact.

---

**Class:** spatial  
**Concept:** rotational  
**Mapping:** unipolar  

**Description:** The presence of angular velocity, curvilinear trajectories, or axial spinning within a physical or spatial concept. Scales from perfectly straight, rigid lines up to chaotic, high-velocity vortices.

---

**Class:** enviornmental  
**Concept:** terrestrial  
**Mapping:** unipolar  

**Description:** Measures association with solid rock, soil, minerals, landmasses, and physical grounding. Scales from ethereal, non-physical, or fluid states up to dense, geological, crystalline, or subterranean mass.

---

**Class:** enviornmental  
**Concept:** gaseousness  
**Mapping:** unipolar  

**Description:** Measures association with atmospheric elements, wind, breath, aerodynamic properties, or vapor. Scales from a vacuum, stagnation, or solid physical density up to high-velocity currents, invisible vapors, or open sky.

---

**Class:** enviornmental  
**Concept:** fluidity  
**Mapping:** unipolar  

**Description:** Measures association with liquid properties, aquatic environments, moisture, and fluid dynamics. Scales from absolute dryness, solidity, or terrestrial nature up to pure oceanic, saturation, or aqueous states.

---

**Class:** enviornmental  
**Concept:** ignition  
**Mapping:** unipolar  

**Description:** Measures association with combustion, thermal energy release, chemical plasma, or radiant heat. Scales from completely inert, flame-retardant, or cold states up to raging, unconstrained incinerations.

---

**Class:** biological  
**Concept:** safety  
**Mapping:** bipolar  

**Description:** Measures the continuum of threat. Negative values represent lethal hazards, catastrophic vulnerability, or immediate peril. Zero represents a neutral, un-threatened baseline. Positive values represent an impenetrable fortress, complete security, or total immunity.

---

**Class:** biological  
**Concept:** shelter  
**Mapping:** unipolar  

**Description:** The degree to which a structure, formation, or environment provides physical protection, security, and habitation against environmental elements or external threats. Scales from complete, exposed vulnerability up to an impenetrable, self-sustained haven.

---

**Class:** biological  
**Concept:** sustenance  
**Mapping:** bipolar  

**Description:** Measures biological utility. Negative values represent toxic, lethal poisons or destructive contaminants. Zero represents non-consumable, biologically inert physical matter. Positive values represent highly nutritious, vital sustaining agents.

---

**Class:** biological  
**Concept:** gender  
**Mapping:** bipolar  

**Description:** Measures semantic, biological, and sociological associations with masculine and feminine archetypes. Negative values represent distinct masculine traits, male biological entities, or patriarchal roles. Zero represents absolute gender-neutrality, inanimate objects, or unisex concepts. Positive values represent distinct feminine traits, female biological entities, or matriarchal roles.

---

**Class:** biological  
**Concept:** audibility  
**Mapping:** unipolar  

**Description:** The structural intensity of sound waves, acoustic properties, or volume levels perceived by an auditory system. Scales from absolute soundless silence up to explosive, deafening sonic force.

---

**Class:** biological  
**Concept:** palatability  
**Mapping:** unipolar  

**Description:** The sensory intensity, flavor concentration, or gustatory appeal of a consumable substance. Scales from completely tasteless, inert matter up to a profound, high-impact flavor profile.

---

**Class:** biological  
**Concept:** olfactibility  
**Mapping:** unipolar  

**Description:** The concentration, presence, or sensory strength of an airborne chemical fragrance, scent, or odor. Scales from completely odorless neutrality up to an overwhelming, dense, or pervasive atmospheric aroma.

---

**Class:** visual  
**Concept:** hue  
**Mapping:** unipolar_normalized  

**Description:** Hue from the HSV color model. Ranges from 0 to 1. This feature is meant for words that represent literal colors such as 'red','blue', or 'magenta.' Apply 0 for any other words.

---

**Class:** visual  
**Concept:** saturation  
**Mapping:** unipolar_normalized  

**Description:** Saturation from the HSV color model. Ranges from 0 to 1. This feature is meant for words that represent literal colors such as 'red','blue', or 'magenta.' Apply 0 for any other words.

---

**Class:** visual  
**Concept:** color_value  
**Mapping:** unipolar_normalized  

**Description:** Value from HSV color model. Ranges from 0 to 1. This feature is meant for words that represent literal colors such as 'red','blue', or 'magenta.' Apply 0 for any other words.

---

**Class:** visual  
**Concept:** transparency  
**Mapping:** unipolar  

**Description:** Measures the degree to which a physical substance, medium, or conceptual barrier allows light, visual information, or matter to pass through it without scattering. Scales from absolute opacity and structural solidity up to perfect, invisible clarity or void-like state.

---

**Class:** agentic  
**Concept:** strength  
**Mapping:** unipolar  

**Description:** Measures association with physical power, muscular force, structural durability, and mechanical leverage. Scales from complete physical frailty, weightlessness, or structural impotence (0.0) up to maximum kinetic force, dense mass, or absolute load-bearing capacity (4.0).

---

**Class:** agentic  
**Concept:** dexterity  
**Mapping:** unipolar  

**Description:** Measures association with fine motor skills, physical agility, spatial precision, and swift reflexes. Scales from total immobility, clumsiness, or rigid inertia (0.0) up to micro-precise articulation, rapid velocity, and flawless physical coordination (4.0).

---

**Class:** agentic  
**Concept:** intelligence  
**Mapping:** unipolar  

**Description:** Measures association with analytical processing, raw data ingestion, logical deduction, and systematic problem-solving. Scales from instinctive reactive states, absolute ignorance, or non-cognitive matter (0.0) up to highly complex computational logic, pattern recognition, and structured academic knowledge (4.0).

---

**Class:** agentic  
**Concept:** wisdom  
**Mapping:** unipolar  

**Description:** Measures association with holistic situational awareness, intuitive judgment, experiential pattern-matching, and philosophical synthesis. Scales from complete naivety, perceptual blindness, or short-sighted recklessness (0.0) up to deep systemic understanding, profound perspective, and acute environmental awareness (4.0).

---

**Class:** agentic  
**Concept:** constitution  
**Mapping:** unipolar  

**Description:** Measures association with biological resilience, systemic endurance, physical vitality, and resistance to environmental degradation or toxins. Scales from extreme vulnerability, cellular decay, or fragile volatility (0.0) up to absolute biological stability, immune optimization, and permanent structural stamina (4.0).

---

