# Agents Directory

This folder contains a collection of **agent skeletons** organised by category.  Each top‑level folder under `agents/` is a fully independent starting point for building your own large language model (LLM) agent.  To keep the repository lean and avoid duplication, the category subfolders (`starter`, `advanced`, `teams`, `rag`) now contain only a brief description and links back to the actual agent code.  You can read the individual `README.md` files in each agent directory for details on what they do and how to extend them.

## Starter Agents

These simple, single‑purpose agents are ideal for learning and quick experimentation:

- **[`summarization_agent`](./summarization_agent)** – condenses long passages of text into concise summaries.
- **[`data_analysis_agent`](./data_analysis_agent)** – loads CSV data, prints descriptive statistics and answers natural‑language questions using `pandasai`.
- **[`travel_itinerary_agent`](./travel_itinerary_agent)** – collects trip details and assembles a synthetic itinerary.
- **[`voice_agent_demo`](./voice_agent_demo)** – listens to your voice, generates a reply and speaks back using `speech_recognition` and `pyttsx3`.
- **[`meme_generator_agent`](./meme_generator_agent)** – overlays a caption onto an image template using Pillow.
- **[`health_fitness_agent`](./health_fitness_agent)** – calculates BMI and offers lifestyle advice.
- **[`breakup_recovery_agent`](./breakup_recovery_agent)** – provides supportive messages for common breakup emotions.
- **[`ai_blog_to_podcast_agent`](./ai_blog_to_podcast_agent)** – converts blog posts into engaging podcast episodes.
- **[`ai_medical_imaging_agent`](./ai_medical_imaging_agent)** – skeleton for processing and analysing medical images.
- **[`ai_music_generator_agent`](./ai_music_generator_agent)** – skeleton for composing music via generative models.
- **[`local_news_agent`](./local_news_agent)** – gathers and summarises local news articles.
- **[`gemini_multimodal_agent_demo`](./gemini_multimodal_agent_demo)** – demonstrates Gemini’s multimodal capabilities with text and image inputs.

## Advanced & Domain‑Specific Agents

These skeletons tackle more sophisticated tasks and can serve as foundations for domain‑specific applications:

- **[`ai_deep_research_agent`](./ai_deep_research_agent)** – conducts in‑depth research across multiple sources and compiles comprehensive reports.
- **[`ai_consultant_agent`](./ai_consultant_agent)** – acts as a domain expert (e.g., marketing, engineering) to provide strategic advice.
- **[`ai_system_architect_agent`](./ai_system_architect_agent)** – designs software or system architectures based on user requirements.
- **[`ai_lead_generation_agent`](./ai_lead_generation_agent)** – identifies and qualifies potential leads for sales and marketing teams.
- **[`ai_financial_coach_agent`](./ai_financial_coach_agent)** – provides personalised financial advice and investment guidance.
- **[`ai_movie_production_agent`](./ai_movie_production_agent)** – coordinates script development, casting suggestions and production planning.
- **[`ai_product_launch_intelligence_agent`](./ai_product_launch_intelligence_agent)** – analyses market trends and competitive landscapes for new product launches.
- **[`ai_journalist_agent`](./ai_journalist_agent)** – generates news articles and press releases with citations and tone analysis.
- **[`ai_meeting_agent`](./ai_meeting_agent)** – summarises meeting transcripts and extracts action items.
- **[`openai_research_agent`](./openai_research_agent)** – demonstrates how to run open‑ended research tasks using the OpenAI API.
- **[`xai_finance_agent`](./xai_finance_agent)** – explores explainable AI techniques applied to financial data.
- **[`web_scrapping_ai_agent`](./web_scrapping_ai_agent)** – performs web scraping to collect information for downstream agents.

  
### Additional advanced & domain‑specific examples

The following agents cover specialised domains and utilities.  Each entry links to a skeleton directory with a concise description:

- **[`document_processing_agent`](./document_processing_agent)** – OCR and text extraction from scanned documents or PDFs.
- **[`sentiment_analysis_agent`](./sentiment_analysis_agent)** – sentiment detection for reviews or social posts.
- **[`technical_translation_agent`](./technical_translation_agent)** – domain‑aware translation of technical documents.
- **[`code_review_agent`](./code_review_agent)** – static analysis and LLM‑generated code improvement suggestions.
- **[`research_synthesizer_agent`](./research_synthesizer_agent)** – retrieval‑augmented synthesis of information from multiple sources.
- **[`academic_paper_analyst_agent`](./academic_paper_analyst_agent)** – extracts insights and metrics from academic papers.
- **[`business_intelligence_agent`](./business_intelligence_agent)** – converts unstructured data into business intelligence dashboards.
- **[`chatbot_training_data_generator_agent`](./chatbot_training_data_generator_agent)** – generates synthetic training dialogues for chatbots.
- **[`compliance_audit_agent`](./compliance_audit_agent)** – automates compliance audits and process checks.
- **[`compliance_checker_agent`](./compliance_checker_agent)** – verifies documents against regulatory requirements.
- **[`creative_story_generator_agent`](./creative_story_generator_agent)** – drafts imaginative stories based on prompts.
- **[`customer_support_agent`](./customer_support_agent)** – triages and answers customer queries.
- **[`expense_report_agent`](./expense_report_agent)** – extracts and organises expense data for reporting.
- **[`financial_statement_analysis_agent`](./financial_statement_analysis_agent)** – summarises key metrics from financial statements.
- **[`grammar_correction_agent`](./grammar_correction_agent)** – corrects grammatical errors in text inputs.
- **[`hr_resume_screening_agent`](./hr_resume_screening_agent)** – screens résumés and highlights top candidates.
- **[`interview_question_generator_agent`](./interview_question_generator_agent)** – compiles customised interview questions.
- **[`legal_contract_summariser_agent`](./legal_contract_summariser_agent)** – condenses legal contracts into key points.
- **[`marketing_campaign_agent`](./marketing_campaign_agent)** – assists in drafting and analysing marketing campaigns.
- **[`meeting_minutes_agent`](./meeting_minutes_agent)** – captures and organises meeting notes and action items.
- **[`personalization_agent`](./personalization_agent)** – tailors content or recommendations for individual users.
- **[`product_recommendation_agent`](./product_recommendation_agent)** – suggests products based on user preferences.
- **[`research_assistant_agent`](./research_assistant_agent)** – automates literature searches and summarisation.
- **[`risk_assessment_agent`](./risk_assessment_agent)** – evaluates risks in projects or decisions.
- **[`sales_email_agent`](./sales_email_agent)** – drafts personalised sales outreach emails.
- **[`scheduling_assistant_agent`](./scheduling_assistant_agent)** – books appointments and manages calendars.
- **[`seo_content_generator_agent`](./seo_content_generator_agent)** – produces search‑optimised content and keywords.
- **[`translation_summarisation_agent`](./translation_summarisation_agent)** – combines translation and summarisation tasks.
- **[`trend_analysis_agent`](./trend_analysis_agent)** – monitors social media and news to detect trends.
- **[`bug_triage_agent`](./bug_triage_agent)** – prioritises bug reports and assigns owners.
- **[`data_visualization_agent`](./data_visualization_agent)** – generates charts and graphs from data sets.
- **[`email_classification_agent`](./email_classification_agent)** – sorts emails into categories like spam or promotions.
- **[`hr_onboarding_agent`](./hr_onboarding_agent)** – automates employee onboarding tasks.
- **[`supply_chain_optimizer_agent`](./supply_chain_optimizer_agent)** – models inventory and logistics for supply chains.
- **[`stock_analysis_agent`](./stock_analysis_agent)** – analyses stock market data and trends.
- **[`climate_change_insight_agent`](./climate_change_insight_agent)** – summarises climate research and data.
- **[`knowledge_graph_builder_agent`](./knowledge_graph_builder_agent)** – constructs knowledge graphs from text.
- **[`network_security_agent`](./network_security_agent)** – monitors logs for security anomalies.
- **[`digital_marketing_strategy_agent`](./digital_marketing_strategy_agent)** – drafts digital marketing strategies.
- **[`chatbot_personality_agent`](./chatbot_personality_agent)** – defines and enforces chatbot personas.
- **[`healthcare_diagnosis_support_agent`](./healthcare_diagnosis_support_agent)** – assists clinicians with differential diagnosis suggestions.
- **[`legal_case_research_agent`](./legal_case_research_agent)** – searches legal databases and summarises cases.
- **[`e_learning_content_generator_agent`](./e_learning_content_generator_agent)** – creates lesson plans and quizzes.
- **[`patient_feedback_analysis_agent`](./patient_feedback_analysis_agent)** – analyses patient comments and sentiment.
- **[`product_feedback_classifier_agent`](./product_feedback_classifier_agent)** – categorises product reviews for actionable insights.
- **[`event_planning_agent`](./event_planning_agent)** – organises event schedules and logistics.
- **[`energy_consumption_optimizer_agent`](./energy_consumption_optimizer_agent)** – analyses energy usage and recommends efficiencies.
- **[`scientific_simulation_agent`](./scientific_simulation_agent)** – runs or interprets scientific simulations.
- **[`architecture_visualisation_agent`](./architecture_visualisation_agent)** – generates diagrams from system descriptions.
- **[`chatbot_analytics_agent`](./chatbot_analytics_agent)** – computes metrics from chatbot conversations.
- **[`news_trend_monitoring_agent`](./news_trend_monitoring_agent)** – watches news feeds to surface emerging topics.
- **[`mental_health_support_agent`](./mental_health_support_agent)** – provides supportive prompts and resources.
- **[`recipe_generation_agent`](./recipe_generation_agent)** – creates cooking recipes from ingredients.
- **[`sport_strategy_agent`](./sport_strategy_agent)** – analyses sports data to suggest tactics.
- **[`environmental_impact_assessment_agent`](./environmental_impact_assessment_agent)** – evaluates sustainability impacts.
- **[`fraud_detection_agent`](./fraud_detection_agent)** – flags anomalies indicative of fraud.
- **[`iot_device_monitoring_agent`](./iot_device_monitoring_agent)** – monitors IoT sensor data and raises alerts.
- **[`remote_learning_assistant_agent`](./remote_learning_assistant_agent)** – schedules study sessions and tracks progress.
- **[`creative_art_generator_agent`](./creative_art_generator_agent)** – generates visual artwork using generative models.
 - **[`philanthropic_project_agent`](./philanthropic_project_agent)** – manages charitable initiatives and reports on impact.

### Infrastructure & interpretability examples

These agents address cross‑cutting concerns such as offline inference,
interpretability, operations and production pipelines:

  - **[`local_inference_agent`](./local_inference_agent)** – runs quantised
    language models on your own hardware using `llama‑cpp‑python`.
  - **[`interpretability_demo_agent`](./interpretability_demo_agent)** –
    demonstrates how to visualise token importances and explain model
    predictions using interpretability libraries.
  - **[`llmops_monitoring_agent`](./llmops_monitoring_agent)** – shows how to
    instrument your agent with monitoring hooks for prompts, responses and
    metrics.
  - **[`production_pipeline_agent`](./production_pipeline_agent)** – provides
    a high‑level template for building data ingestion, inference and
    post‑processing pipelines around an LLM.

## Voice & game agents

These examples showcase agents that interact via speech or play games:

- **[`voice_summary_agent`](./voice_summary_agent)** – listens to audio, transcribes it and summarises the content.
- **[`ai_audio_tour_agent`](./ai_audio_tour_agent)** – generates narrated tours for museums, cities or landmarks.
- **[`customer_support_voice_agent`](./customer_support_voice_agent)** – answers spoken customer queries and logs issues.
- **[`voice_rag_agent`](./voice_rag_agent)** – combines voice input with retrieval‑augmented generation and speaks the answer.
- **[`browser_mcp_agent`](./browser_mcp_agent)** – controls a web browser through the Model Context Protocol.
- **[`tic_tac_toe_agent`](./tic_tac_toe_agent)** – plays tic‑tac‑toe and serves as a template for autonomous game agents.

## MCP agents

These skeletons demonstrate the Model Context Protocol (MCP) for interacting
with external systems:

- **[`browser_mcp_agent`](./browser_mcp_agent)** – controls a web browser to automate navigation and form filling.
- **[`github_mcp_agent`](./github_mcp_agent)** – reads, writes and manages code in GitHub repositories.
- **[`notion_mcp_agent`](./notion_mcp_agent)** – creates and updates pages and databases in Notion.
- **[`travel_planner_mcp_agent_team`](./travel_planner_mcp_agent_team)** – multi‑agent team that plans trips using MCP‑enabled services.

## Multi‑Agent Teams

These examples show how multiple agents can collaborate as teams, each playing a specialised role:

- **[`ai_competitor_intelligence_agent_team`](./ai_competitor_intelligence_agent_team)** – researches competitors, analyses market positioning and synthesises findings.
- **[`ai_finance_agent_team`](./ai_finance_agent_team)** – coordinates budgeting, forecasting and reporting tasks across multiple agents.
- **[`ai_teaching_agent_team`](./ai_teaching_agent_team)** – develops lesson plans, delivers content and assesses learner progress.
- **[`mixture_of_agents`](./mixture_of_agents)** – demonstrates coordinating diverse agent types for a single task.
- **[`multi_agent_team`](./multi_agent_team)** – general template for building and orchestrating teams of agents.

## Retrieval‑Augmented Generation (RAG)

Retrieval‑augmented examples combine LLMs with external knowledge sources or memory:

- **[`rag_doc_qa`](./rag_doc_qa)** – indexes local documents and answers questions using a summariser.  This skeleton illustrates a basic RAG pipeline that fetches passages, ranks them and generates a consolidated answer.

The `rag` subfolder contains a README with further guidance on building your own RAG pipelines.

---

If you’re unsure where to start, we recommend trying a **starter agent** first.  When you’re ready to explore more complex workflows, dive into the advanced agents or multi‑agent teams.  For background information on agents and best practices, see the [Beginner’s Guide](../docs/beginners_guide.md).