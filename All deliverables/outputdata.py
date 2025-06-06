"""
Here using CHATGPT i have converted each urls along with the variables in a structured format so that i can present my output
in csv file .
"""


import csv

import ast

data = [
 {
    "ID": "Netclan20241017",
    "URL": "https://insights.blackcoffer.com/ai-and-ml-based-youtube-analytics-and-content-creation-tool-for-optimizing-subscriber-engagement-and-content-strategy/",
    "Analysis": { "positive_score": 19,"negative_score": -3,"polarity_score": 0.7272723966943652,"subjectivity_score": 0.05744125176393599,"avg_sentence_length": 383.0,"percentage_complex_words": 57.96344647519582,"fog_index": 176.38537859007835,"complex_word_count": 222,"word_count": 383,"syllables_per_word": 3.2610966057441253, "personal_pronouns": 0,"avg_word_length": 8.219321148825065}
  },
  {
    "ID": "Netclan20241018",
    "URL": "https://insights.blackcoffer.com/enhancing-front-end-features-and-functionality-for-improved-user-experience-and-dashboard-accuracy-in-partner-hospital-application/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -7,
      "polarity_score": 0.5483869198751872,
      "subjectivity_score": 0.05227655898353189,
      "avg_sentence_length": 593.0,
      "percentage_complex_words": 50.42158516020236,
      "fog_index": 257.36863406408094,
      "complex_word_count": 299,
      "word_count": 593,
      "syllables_per_word": 2.903878583473862,
      "personal_pronouns": 0,
      "avg_word_length": 7.54637436762226
    }
  },
  {
    "ID": "Netclan20241019",
    "URL": "https://insights.blackcoffer.com/roas-dashboard-for-campaign-wise-google-ads-budget-tracking-using-google-ads-ap/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -7,
      "polarity_score": 0.5757574012856359,
      "subjectivity_score": 0.06804123571048999,
      "avg_sentence_length": 485.0,
      "percentage_complex_words": 52.98969072164949,
      "fog_index": 215.1958762886598,
      "complex_word_count": 257,
      "word_count": 485,
      "syllables_per_word": 3.0,
      "personal_pronouns": 0,
      "avg_word_length": 7.692783505154639,
      "url_id": "Netclan20241019"
    }
  },
  {
    "ID": "Netclan20241020",
    "URL": "https://insights.blackcoffer.com/efficient-processing-and-analysis-of-financial-data-from-pdf-files-addressing-formatting-inconsistencies-and-ensuring-data-integrity-for-a-toyota-dealership-management-firm/",
    "Analysis": {
      "positive_score": 37,
      "negative_score": -13,
      "polarity_score": 0.4799999040000192,
      "subjectivity_score": 0.08347245269662015,
      "avg_sentence_length": 599.0,
      "percentage_complex_words": 61.93656093489148,
      "fog_index": 264.37462437395664,
      "complex_word_count": 371,
      "word_count": 599,
      "syllables_per_word": 3.1385642737896493,
      "personal_pronouns": 0,
      "avg_word_length": 8.128547579298832,
      "url_id": "Netclan20241020"
    }
  },
  {
    "ID": "Netclan20241021",
    "URL": "https://insights.blackcoffer.com/development-of-ea-robot-for-automated-trading/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -3,
      "polarity_score": 0.7692304733728949,
      "subjectivity_score": 0.044217686322828464,
      "avg_sentence_length": 588.0,
      "percentage_complex_words": 47.95918367346938,
      "fog_index": 254.38367346938776,
      "complex_word_count": 282,
      "word_count": 588,
      "syllables_per_word": 2.945578231292517,
      "personal_pronouns": 0,
      "avg_word_length": 7.489795918367347,
      "url_id": "Netclan20241021"
    }
  },


        {
    "ID": "Netclan20241022",
    "URL": "https://insights.blackcoffer.com/ai-and-ml-based-youtube-analytics-and-content-creation-tool-for-optimizing-subscriber-engagement-and-content-strategy/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -3,
      "polarity_score": 0.7272723966943652,
      "subjectivity_score": 0.05744125176393599,
      "avg_sentence_length": 383.0,
      "percentage_complex_words": 57.96344647519582,
      "fog_index": 176.38537859007835,
      "complex_word_count": 222,
      "word_count": 383,
      "syllables_per_word": 3.2610966057441253,
      "personal_pronouns": 0,
      "avg_word_length": 8.219321148825065,
      "url_id": "Netclan20241022"
    }
  },
  {
    "ID": "Netclan20241023",
    "URL": "https://insights.blackcoffer.com/enhancing-front-end-features-and-functionality-for-improved-user-experience-and-dashboard-accuracy-in-partner-hospital-application/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -7,
      "polarity_score": 0.5483869198751872,
      "subjectivity_score": 0.05227655898353189,
      "avg_sentence_length": 593.0,
      "percentage_complex_words": 50.42158516020236,
      "fog_index": 257.36863406408094,
      "complex_word_count": 299,
      "word_count": 593,
      "syllables_per_word": 2.903878583473862,
      "personal_pronouns": 0,
      "avg_word_length": 7.54637436762226,
      "url_id": "Netclan20241023"
    }
  },
  {
    "ID": "Netclan20241024",
    "URL": "https://insights.blackcoffer.com/roas-dashboard-for-campaign-wise-google-ads-budget-tracking-using-google-ads-ap/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -7,
      "polarity_score": 0.5757574012856359,
      "subjectivity_score": 0.06804123571048999,
      "avg_sentence_length": 485.0,
      "percentage_complex_words": 52.98969072164949,
      "fog_index": 215.1958762886598,
      "complex_word_count": 257,
      "word_count": 485,
      "syllables_per_word": 3.0,
      "personal_pronouns": 0,
      "avg_word_length": 7.692783505154639,
      "url_id": "Netclan20241024"
    }
  },
  {
    "ID": "Netclan20241025",
    "URL": "https://insights.blackcoffer.com/efficient-processing-and-analysis-of-financial-data-from-pdf-files-addressing-formatting-inconsistencies-and-ensuring-data-integrity-for-a-toyota-dealership-management-firm/",
    "Analysis": {
      "positive_score": 37,
      "negative_score": -13,
      "polarity_score": 0.4799999040000192,
      "subjectivity_score": 0.08347245269662015,
      "avg_sentence_length": 599.0,
      "percentage_complex_words": 61.93656093489148,
      "fog_index": 264.37462437395664,
      "complex_word_count": 371,
      "word_count": 599,
      "syllables_per_word": 3.1385642737896493,
      "personal_pronouns": 0,
      "avg_word_length": 8.128547579298832,
      "url_id": "Netclan20241025"
    }
  },
  {
    "ID": "Netclan20241026",
    "URL": "https://insights.blackcoffer.com/transforming-and-managing-a-large-scale-sql-pedigree-database-to-neo4j-graph-db/",
    "Analysis": {
      "positive_score": 67,
      "negative_score": -12,
      "polarity_score": 0.696202443518678,
      "subjectivity_score": 0.07149321202268587,
      "avg_sentence_length": 1105.0,
      "percentage_complex_words": 62.62443438914027,
      "fog_index": 467.04977375565613,
      "complex_word_count": 692,
      "word_count": 1105,
      "syllables_per_word": 3.0986425339366517,
      "personal_pronouns": 0,
      "avg_word_length": 7.870588235294117,
      "url_id": "Netclan20241026"
    }
  },
   {
    "ID": "Netclan20241027",
    "URL": "https://insights.blackcoffer.com/enhancing-model-accuracy-from-58-to-over-90-strategies-for-improving-predictive-performance/",
    "Analysis": {
      "positive_score": 37,
      "negative_score": -7,
      "polarity_score": 0.6818180268595393,
      "subjectivity_score": 0.08712871114596613,
      "avg_sentence_length": 505.0,
      "percentage_complex_words": 62.97029702970297,
      "fog_index": 227.18811881188117,
      "complex_word_count": 318,
      "word_count": 505,
      "syllables_per_word": 3.243564356435644,
      "personal_pronouns": 0,
      "avg_word_length": 8.184158415841583,
      "url_id": "Netclan20241027"
    }
  },
  {
    "ID": "Netclan20241028",
    "URL": "https://insights.blackcoffer.com/securing-sensitive-financial-data-with-privacy-preserving-machine-learning-for-predictive-analytics/",
    "Analysis": {
      "positive_score": 41,
      "negative_score": -4,
      "polarity_score": 0.8222220395062134,
      "subjectivity_score": 0.07666098676897808,
      "avg_sentence_length": 587.0,
      "percentage_complex_words": 64.90630323679727,
      "fog_index": 260.7625212947189,
      "complex_word_count": 381,
      "word_count": 587,
      "syllables_per_word": 3.2759795570698467,
      "personal_pronouns": 0,
      "avg_word_length": 8.318568994889267,
      "url_id": "Netclan20241028"
    }
  },
  {
    "ID": "Netclan20241029",
    "URL": "https://insights.blackcoffer.com/enhancing-data-collection-for-research-institutions-addressing-survey-fatigue-and-incorporating-verbal-communication-for-richer-insights/",
    "Analysis": {
      "positive_score": 34,
      "negative_score": -9,
      "polarity_score": 0.58139521362902,
      "subjectivity_score": 0.0861723429624781,
      "avg_sentence_length": 499.0,
      "percentage_complex_words": 59.719438877755515,
      "fog_index": 223.4877755511022,
      "complex_word_count": 298,
      "word_count": 499,
      "syllables_per_word": 3.2304609218436875,
      "personal_pronouns": 0,
      "avg_word_length": 8.226452905811623,
      "url_id": "Netclan20241029"
    }
  },
  {
    "ID": "Netclan20241030",
    "URL": "https://insights.blackcoffer.com/analyzing-the-impact-of-positive-emotions-and-pandemic-severity-on-mental-health-and-resilience-among-entrepreneurs-insights-and-predictive-modeling/",
    "Analysis": {
      "positive_score": 33,
      "negative_score": -10,
      "polarity_score": 0.5348835965386984,
      "subjectivity_score": 0.08634537979226145,
      "avg_sentence_length": 498.0,
      "percentage_complex_words": 61.84738955823293,
      "fog_index": 223.9389558232932,
      "complex_word_count": 308,
      "word_count": 498,
      "syllables_per_word": 3.281124497991968,
      "personal_pronouns": 0,
      "avg_word_length": 8.271084337349398,
      "url_id": "Netclan20241030"
    }
  },
  {
    "ID": "Netclan20241031",
    "URL": "https://insights.blackcoffer.com/dynamic-brand-centric-dashboard-for-automotive-dealerships-pdf-to-financial-insights-with-flask-react-architecture-and-aws-cloud-hosting/",
    "Analysis": {
      "positive_score": 66,
      "negative_score": -23,
      "polarity_score": 0.48314601312966143,
      "subjectivity_score": 0.10372960252063401,
      "avg_sentence_length": 858.0,
      "percentage_complex_words": 55.71095571095571,
      "fog_index": 365.48438228438226,
      "complex_word_count": 478,
      "word_count": 858,
      "syllables_per_word": 2.9976689976689976,
      "personal_pronouns": 0,
      "avg_word_length": 7.861305361305361,
      "url_id": "Netclan20241031"
    }
  },
  
  {
    "ID": "Netclan20241032",
    "URL": "https://insights.blackcoffer.com/cloud-based-data-modeling-and-analysis-platform-with-drag-and-drop-interface-and-openai-api-integration-for-simulation-insights/",
    "Analysis": {
      "positive_score": 36,
      "negative_score": -9,
      "polarity_score": 0.5999998666666962,
      "subjectivity_score": 0.0692307681656805,
      "avg_sentence_length": 650.0,
      "percentage_complex_words": 56.769230769230774,
      "fog_index": 282.7076923076923,
      "complex_word_count": 369,
      "word_count": 650,
      "syllables_per_word": 3.043076923076923,
      "personal_pronouns": 0,
      "avg_word_length": 7.718461538461538,
      "url_id": "Netclan20241032"
    }
  },
  {
    "ID": "Netclan20241033",
    "URL": "https://insights.blackcoffer.com/voter-profile-analysis-and-search-application-for-targeted-campaign-engagement-using-government-voter-data/",
    "Analysis": {
      "positive_score": 83,
      "negative_score": -10,
      "polarity_score": 0.7849461521563277,
      "subjectivity_score": 0.09046692519001046,
      "avg_sentence_length": 1028.0,
      "percentage_complex_words": 60.311284046692606,
      "fog_index": 435.3245136186771,
      "complex_word_count": 620,
      "word_count": 1028,
      "syllables_per_word": 3.1332684824902723,
      "personal_pronouns": 0,
      "avg_word_length": 7.955252918287938,
      "url_id": "Netclan20241033"
    }
  },
  {
    "ID": "Netclan20241034",
    "URL": "https://insights.blackcoffer.com/bert-based-classification-of-individuals-and-organizations-into-two-categories-using-natural-language-processing/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -3,
      "polarity_score": 0.7499996875001302,
      "subjectivity_score": 0.059850372572309914,
      "avg_sentence_length": 401.0,
      "percentage_complex_words": 58.85286783042394,
      "fog_index": 183.9411471321696,
      "complex_word_count": 236,
      "word_count": 401,
      "syllables_per_word": 3.319201995012469,
      "personal_pronouns": 0,
      "avg_word_length": 8.314214463840399,
      "url_id": "Netclan20241034"
    }
  },
  {
    "ID": "Netclan20241035",
    "URL": "https://insights.blackcoffer.com/comprehensive-analysis-of-solana-and-ethereum-contributors-using-github-api-with-comparative-study-of-1000-random-github-profiles/",
    "Analysis": {
      "positive_score": 59,
      "negative_score": -11,
      "polarity_score": 0.6857141877551161,
      "subjectivity_score": 0.10432190604587324,
      "avg_sentence_length": 671.0,
      "percentage_complex_words": 54.24739195230999,
      "fog_index": 290.09895678092397,
      "complex_word_count": 364,
      "word_count": 671,
      "syllables_per_word": 3.076005961251863,
      "personal_pronouns": 0,
      "avg_word_length": 7.75558867362146,
      "url_id": "Netclan20241035"
    }
  },
  {
    "ID": "Netclan20241036",
    "URL": "https://insights.blackcoffer.com/powerbi-rest-api-fetching-dataflow-and-refresh-schedules-with-semantic-models/",
    "Analysis": {
      "positive_score": 51,
      "negative_score": -5,
      "polarity_score": 0.8214284247449241,
      "subjectivity_score": 0.09824561231148049,
      "avg_sentence_length": 570.0,
      "percentage_complex_words": 54.56140350877193,
      "fog_index": 249.8245614035088,
      "complex_word_count": 311,
      "word_count": 570,
      "syllables_per_word": 3.087719298245614,
      "personal_pronouns": 0,
      "avg_word_length": 7.780701754385965,
      "url_id": "Netclan20241036"
    }
  },
  {
    "ID": "Netclan20241037",
    "URL": "https://insights.blackcoffer.com/automated-job-data-import-and-management-solution-for-enhanced-efficiency/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -2,
      "polarity_score": 0.8571425510205175,
      "subjectivity_score": 0.06466512552736431,
      "avg_sentence_length": 433.0,
      "percentage_complex_words": 55.42725173210161,
      "fog_index": 195.37090069284065,
      "complex_word_count": 240,
      "word_count": 433,
      "syllables_per_word": 3.136258660508083,
      "personal_pronouns": 0,
      "avg_word_length": 7.819861431870669,
      "url_id": "Netclan20241037"
    }
  },
  
  {
    "ID": "Netclan20241038",
    "URL": "https://insights.blackcoffer.com/data-analytics-and-optimization-solution-for-enhancing-renewable-energy-efficiency/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -2,
      "polarity_score": 0.8518515363512829,
      "subjectivity_score": 0.06293706146999857,
      "avg_sentence_length": 429.0,
      "percentage_complex_words": 59.90675990675991,
      "fog_index": 195.56270396270398,
      "complex_word_count": 257,
      "word_count": 429,
      "syllables_per_word": 3.2587412587412588,
      "personal_pronouns": 0,
      "avg_word_length": 8.195804195804195,
      "url_id": "Netclan20241038"
    }
  },
  {
    "ID": "Netclan20241039",
    "URL": "https://insights.blackcoffer.com/time-series-analysis-and-trend-forecasting-solution-for-predicting-news-trends/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -2,
      "polarity_score": 0.8571425510205175,
      "subjectivity_score": 0.06496519570846414,
      "avg_sentence_length": 431.0,
      "percentage_complex_words": 57.30858468677494,
      "fog_index": 195.32343387471,
      "complex_word_count": 247,
      "word_count": 431,
      "syllables_per_word": 3.1693735498839906,
      "personal_pronouns": 0,
      "avg_word_length": 8.076566125290023,
      "url_id": "Netclan20241039"
    }
  },
  {
    "ID": "Netclan20241040",
    "URL": "https://insights.blackcoffer.com/advanced-data-visualization-solutions-for-monitoring-key-business-metrics-with-integrated-interactive-dashboards/",
    "Analysis": {
      "positive_score": 32,
      "negative_score": -1,
      "polarity_score": 0.9393936547291954,
      "subjectivity_score": 0.07875894800097977,
      "avg_sentence_length": 419.0,
      "percentage_complex_words": 62.29116945107399,
      "fog_index": 192.5164677804296,
      "complex_word_count": 261,
      "word_count": 419,
      "syllables_per_word": 3.307875894988067,
      "personal_pronouns": 0,
      "avg_word_length": 8.221957040572793,
      "url_id": "Netclan20241040"
    }
  },
  {
    "ID": "Netclan20241041",
    "URL": "https://insights.blackcoffer.com/advanced-patient-data-analysis-solution-for-trend-identification-and-improved-healthcare-outcome/",
    "Analysis": {
      "positive_score": 41,
      "negative_score": -3,
      "polarity_score": 0.8636361673554165,
      "subjectivity_score": 0.10185184949417016,
      "avg_sentence_length": 432.0,
      "percentage_complex_words": 61.342592592592595,
      "fog_index": 197.33703703703705,
      "complex_word_count": 265,
      "word_count": 432,
      "syllables_per_word": 3.2777777777777777,
      "personal_pronouns": 0,
      "avg_word_length": 8.226851851851851,
      "url_id": "Netclan20241041"
    }
  },
  {
    "ID": "Netclan20241042",
    "URL": "https://insights.blackcoffer.com/anomaly-detection-and-analysis-for-enhanced-data-integrity-and-user-experience-on-bright-datas-website/",
    "Analysis": {
      "positive_score": 32,
      "negative_score": -10,
      "polarity_score": 0.5238093990930002,
      "subjectivity_score": 0.09502262228455606,
      "avg_sentence_length": 442.0,
      "percentage_complex_words": 58.371040723981906,
      "fog_index": 200.14841628959277,
      "complex_word_count": 258,
      "word_count": 442,
      "syllables_per_word": 3.171945701357466,
      "personal_pronouns": 0,
      "avg_word_length": 7.995475113122172,
      "url_id": "Netclan20241042"
    }
  },
  
  {
    "ID": "Netclan20241043",
    "URL": "https://insights.blackcoffer.com/building-custom-tflite-models-and-benchmarking-on-voxl2-chips/",
    "Analysis": {
      "positive_score": 30,
      "negative_score": -2,
      "polarity_score": 0.8749997265625854,
      "subjectivity_score": 0.05306799248643462,
      "avg_sentence_length": 603.0,
      "percentage_complex_words": 53.39966832504146,
      "fog_index": 262.55986733001663,
      "complex_word_count": 322,
      "word_count": 603,
      "syllables_per_word": 2.966832504145937,
      "personal_pronouns": 0,
      "avg_word_length": 7.8059701492537314,
      "url_id": "Netclan20241043"
    }
  },
  {
    "ID": "Netclan20241044",
    "URL": "https://insights.blackcoffer.com/sports-prediction-model-for-multiple-sports-leagues/",
    "Analysis": {
      "positive_score": 36,
      "negative_score": -8,
      "polarity_score": 0.63636349173557,
      "subjectivity_score": 0.06821705320593716,
      "avg_sentence_length": 645.0,
      "percentage_complex_words": 52.4031007751938,
      "fog_index": 278.9612403100775,
      "complex_word_count": 338,
      "word_count": 645,
      "syllables_per_word": 2.924031007751938,
      "personal_pronouns": 0,
      "avg_word_length": 7.634108527131783,
      "url_id": "Netclan20241044"
    }
  },
  {
    "ID": "Netclan20241045",
    "URL": "https://insights.blackcoffer.com/efficient-coach-allocation-system-for-sports-coaching-organization/",
    "Analysis": {
      "positive_score": 32,
      "negative_score": -7,
      "polarity_score": 0.6410254766601341,
      "subjectivity_score": 0.06180665512192306,
      "avg_sentence_length": 631.0,
      "percentage_complex_words": 57.52773375594295,
      "fog_index": 275.4110935023772,
      "complex_word_count": 363,
      "word_count": 631,
      "syllables_per_word": 3.0649762282091917,
      "personal_pronouns": 0,
      "avg_word_length": 7.866877971473851,
      "url_id": "Netclan20241045"
    }
  },
  {
    "ID": "Netclan20241046",
    "URL": "https://insights.blackcoffer.com/data-studio-dashboard-with-a-data-pipeline-tool-synced-with-podio-using-custom-webhooks-and-google-cloud-function-2/",
    "Analysis": {
      "positive_score": 38,
      "negative_score": -13,
      "polarity_score": 0.4901959823145132,
      "subjectivity_score": 0.0766917281700492,
      "avg_sentence_length": 665.0,
      "percentage_complex_words": 58.04511278195489,
      "fog_index": 289.21804511278197,
      "complex_word_count": 386,
      "word_count": 665,
      "syllables_per_word": 3.0270676691729324,
      "personal_pronouns": 0,
      "avg_word_length": 7.616541353383458,
      "url_id": "Netclan20241046"
    }
  },
  {
    "ID": "Netclan20241047",
    "URL": "https://insights.blackcoffer.com/ai-driven-backend-for-audio-to-text-conversion-and-analytical-assessment-in-pharmaceutical-practice/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": -8,
      "polarity_score": 0.5897434385273234,
      "subjectivity_score": 0.06701030812697065,
      "avg_sentence_length": 582.0,
      "percentage_complex_words": 58.76288659793815,
      "fog_index": 256.30515463917527,
      "complex_word_count": 342,
      "word_count": 582,
      "syllables_per_word": 3.104810996563574,
      "personal_pronouns": 0,
      "avg_word_length": 7.938144329896907,
      "url_id": "Netclan20241047"
    }
  },
  
  {
    "ID": "Netclan20241048",
    "URL": "https://insights.blackcoffer.com/cloud-based-web-application-for-financial-data-processing-and-visualization-of-sp-500-metrics/",
    "Analysis": {
      "positive_score": 68,
      "negative_score": -14,
      "polarity_score": 0.6585365050565237,
      "subjectivity_score": 0.11341631931651011,
      "avg_sentence_length": 723.0,
      "percentage_complex_words": 57.53803596127247,
      "fog_index": 312.215214384509,
      "complex_word_count": 416,
      "word_count": 723,
      "syllables_per_word": 3.1341632088520055,
      "personal_pronouns": 0,
      "avg_word_length": 8.029045643153527,
      "url_id": "Netclan20241048"
    }
  },
  {
    "ID": "Netclan20241049",
    "URL": "https://insights.blackcoffer.com/department-wise-kpi-tracking-dashboard-with-technician-performance-analysis-for-atoz-dependable-service/",
    "Analysis": {
      "positive_score": 40,
      "negative_score": -5,
      "polarity_score": 0.7777776049383099,
      "subjectivity_score": 0.057989689974359666,
      "avg_sentence_length": 776.0,
      "percentage_complex_words": 52.83505154639175,
      "fog_index": 331.5340206185567,
      "complex_word_count": 410,
      "word_count": 776,
      "syllables_per_word": 2.990979381443299,
      "personal_pronouns": 0,
      "avg_word_length": 7.666237113402062,
      "url_id": "Netclan20241049"
    }
  },
  {
    "ID": "Netclan20241050",
    "URL": "https://insights.blackcoffer.com/steps-to-convert-a-node-js-api-to-python-for-aws-lambda-deployment/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": 6,
      "polarity_score": 0.6756754930606775,
      "subjectivity_score": 0.07254901818531337,
      "avg_sentence_length": 510.0,
      "percentage_complex_words": 55.68627450980392,
      "fog_index": 226.2745098039216,
      "complex_word_count": 284,
      "word_count": 510,
      "syllables_per_word": 3.0392156862745097,
      "personal_pronouns": 0,
      "avg_word_length": 7.890196078431373,
      "url_id": "Netclan20241050"
    }
  },
  {
    "ID": "Netclan20241051",
    "URL": "https://insights.blackcoffer.com/building-an-analytics-dashboard-with-a-pdf-parsing-pipeline-for-data-extraction/",
    "Analysis": {
      "positive_score": 50,
      "negative_score": -19,
      "polarity_score": 0.44927529720647863,
      "subjectivity_score": 0.06920762217444712,
      "avg_sentence_length": 997.0,
      "percentage_complex_words": 53.56068204613842,
      "fog_index": 420.2242728184554,
      "complex_word_count": 534,
      "word_count": 997,
      "syllables_per_word": 2.924774322968907,
      "personal_pronouns": 0,
      "avg_word_length": 7.707121364092277,
      "url_id": "Netclan20241051"
    }
  },
  {
    "ID": "Netclan20241052",
    "URL": "https://insights.blackcoffer.com/building-a-real-time-log-file-visualization-dashboard-in-kibana/",
    "Analysis": {
      "positive_score": 34,
      "negative_score": -23,
      "polarity_score": 0.19298242228378557,
      "subjectivity_score": 0.07755101935304735,
      "avg_sentence_length": 735.0,
      "percentage_complex_words": 52.51700680272109,
      "fog_index": 315.00680272108843,
      "complex_word_count": 386,
      "word_count": 735,
      "syllables_per_word": 2.9782312925170067,
      "personal_pronouns": 0,
      "avg_word_length": 7.619047619047619,
      "url_id": "Netclan20241052"
    }
  },
  {
    "ID": "Netclan20241053",
    "URL": "https://insights.blackcoffer.com/analyzing-the-impact-of-female-ceo-appointments-on-company-stock-prices/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": -6,
      "polarity_score": 0.6756754930606775,
      "subjectivity_score": 0.05263157819869733,
      "avg_sentence_length": 703.0,
      "percentage_complex_words": 59.45945945945946,
      "fog_index": 304.9837837837838,
      "complex_word_count": 418,
      "word_count": 703,
      "syllables_per_word": 3.132290184921764,
      "personal_pronouns": 0,
      "avg_word_length": 8.054054054054054,
      "url_id": "Netclan20241053"
    }
  },
  {
    "ID": "Netclan20241054",
    "URL": "https://insights.blackcoffer.com/ai-chatbot-using-llm-langchain-llama/",
    "Analysis": {
      "positive_score": 54,
      "negative_score": -7,
      "polarity_score": 0.7704916769685775,
      "subjectivity_score": 0.08472222104552471,
      "avg_sentence_length": 720.0,
      "percentage_complex_words": 53.19444444444444,
      "fog_index": 309.2777777777778,
      "complex_word_count": 383,
      "word_count": 720,
      "syllables_per_word": 3.077777777777778,
      "personal_pronouns": 0,
      "avg_word_length": 7.754166666666666,
      "url_id": "Netclan20241054"
    }
  },
  {
    "ID": "Netclan20241055",
    "URL": "https://insights.blackcoffer.com/healthcare-ai-chatbot-using-llama-llm-langchain/",
    "Analysis": {
      "positive_score": 43,
      "negative_score": -13,
      "polarity_score": 0.5357141900510375,
      "subjectivity_score": 0.07756232579553565,
      "avg_sentence_length": 722.0,
      "percentage_complex_words": 48.89196675900277,
      "fog_index": 308.35678670360113,
      "complex_word_count": 353,
      "word_count": 722,
      "syllables_per_word": 2.8781163434903045,
      "personal_pronouns": 0,
      "avg_word_length": 7.292243767313019,
      "url_id": "Netclan20241055"
    }
  },
  {
    "ID": "Netclan20241056",
    "URL": "https://insights.blackcoffer.com/ai-bot-audio-to-audio/",
    "Analysis": {
      "positive_score": 16,
      "negative_score": 0,
      "polarity_score": 0.9999993750003906,
      "subjectivity_score": 0.036866358597549345,
      "avg_sentence_length": 434.0,
      "percentage_complex_words": 49.07834101382488,
      "fog_index": 193.23133640553,
      "complex_word_count": 213,
      "word_count": 434,
      "syllables_per_word": 3.0506912442396312,
      "personal_pronouns": 0,
      "avg_word_length": 7.658986175115207,
      "url_id": "Netclan20241056"
    }
  },
  {
    "ID": "Netclan20241057",
    "URL": "https://insights.blackcoffer.com/recommendation-engine-for-insurance-sector-to-expand-business-in-the-rural-area/",
    "Analysis": {
      "positive_score": 28,
      "negative_score": -6,
      "polarity_score": 0.647058633218049,
      "subjectivity_score": 0.0640301306209015,
      "avg_sentence_length": 531.0,
      "percentage_complex_words": 56.12052730696798,
      "fog_index": 234.84821092278722,
      "complex_word_count": 298,
      "word_count": 531,
      "syllables_per_word": 3.105461393596987,
      "personal_pronouns": 0,
      "avg_word_length": 7.9491525423728815,
      "url_id": "Netclan20241057"
    }
  },
  {
    "ID": "Netclan20241058",
    "URL": "https://insights.blackcoffer.com/data-from-crm-via-zapier-to-google-sheets-dynamic-to-powerbi/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -4,
      "polarity_score": 0.724137681331834,
      "subjectivity_score": 0.0719602959811341,
      "avg_sentence_length": 403.0,
      "percentage_complex_words": 51.36476426799007,
      "fog_index": 181.74590570719602,
      "complex_word_count": 207,
      "word_count": 403,
      "syllables_per_word": 3.0595533498759306,
      "personal_pronouns": 0,
      "avg_word_length": 7.71712158808933,
      "url_id": "Netclan20241058"
    }
  },
    
  {
    "ID": "Netclan20241059",
    "URL": "https://insights.blackcoffer.com/data-warehouse-to-google-data-studio-looker-dashboard/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": 0,
      "polarity_score": 0.9999995238097505,
      "subjectivity_score": 0.05147058697376013,
      "avg_sentence_length": 408.0,
      "percentage_complex_words": 54.90196078431373,
      "fog_index": 185.1607843137255,
      "complex_word_count": 224,
      "word_count": 408,
      "syllables_per_word": 3.1372549019607843,
      "personal_pronouns": 0,
      "avg_word_length": 7.875,
      "url_id": "Netclan20241059"
    }
  },
  {
    "ID": "Netclan20241060",
    "URL": "https://insights.blackcoffer.com/crm-monday-com-via-zapier-to-power-bi-dashboard/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -5,
      "polarity_score": 0.6774191363164076,
      "subjectivity_score": 0.07616707429564928,
      "avg_sentence_length": 407.0,
      "percentage_complex_words": 49.631449631449634,
      "fog_index": 182.65257985257986,
      "complex_word_count": 202,
      "word_count": 407,
      "syllables_per_word": 2.9705159705159705,
      "personal_pronouns": 0,
      "avg_word_length": 7.606879606879607,
      "url_id": "Netclan20241060"
    }
  },
  {
    "ID": "Netclan20241061",
    "URL": "https://insights.blackcoffer.com/monday-com-to-kpi-dashboard-to-manage-view-and-generate-insights-from-the-crm-data/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": -8,
      "polarity_score": 0.5897434385273234,
      "subjectivity_score": 0.08863636162190087,
      "avg_sentence_length": 440.0,
      "percentage_complex_words": 52.04545454545455,
      "fog_index": 196.81818181818184,
      "complex_word_count": 229,
      "word_count": 440,
      "syllables_per_word": 2.9795454545454545,
      "personal_pronouns": 0,
      "avg_word_length": 7.709090909090909,
      "url_id": "Netclan20241061"
    }
  },
  {
    "ID": "Netclan20241062",
    "URL": "https://insights.blackcoffer.com/data-management-for-a-political-saas-application/",
    "Analysis": {
      "positive_score": 33,
      "negative_score": -5,
      "polarity_score": 0.7368419113573916,
      "subjectivity_score": 0.05234159707518461,
      "avg_sentence_length": 726.0,
      "percentage_complex_words": 50.0,
      "fog_index": 310.40000000000003,
      "complex_word_count": 363,
      "word_count": 726,
      "syllables_per_word": 2.8636363636363638,
      "personal_pronouns": 0,
      "avg_word_length": 7.443526170798898,
      "url_id": "Netclan20241062"
    }
  },
  {
    "ID": "Netclan20241063",
    "URL": "https://insights.blackcoffer.com/google-lsa-ads-google-local-service-ads-etl-tools-and-dashboards/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -4,
      "polarity_score": 0.6799997280001088,
      "subjectivity_score": 0.05387930918363558,
      "avg_sentence_length": 464.0,
      "percentage_complex_words": 54.0948275862069,
      "fog_index": 207.23793103448276,
      "complex_word_count": 251,
      "word_count": 464,
      "syllables_per_word": 3.0668103448275863,
      "personal_pronouns": 0,
      "avg_word_length": 7.795258620689655,
      "url_id": "Netclan20241063"
    }
  },
  
  {
    "ID": "Netclan20241064",
    "URL": "https://insights.blackcoffer.com/ad-networks-marketing-campaign-data-dashboard-in-looker-google-data-studio/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -5,
      "polarity_score": 0.6666664444445185,
      "subjectivity_score": 0.055350552484307154,
      "avg_sentence_length": 542.0,
      "percentage_complex_words": 52.398523985239855,
      "fog_index": 237.75940959409596,
      "complex_word_count": 284,
      "word_count": 542,
      "syllables_per_word": 2.970479704797048,
      "personal_pronouns": 0,
      "avg_word_length": 7.608856088560886,
      "url_id": "Netclan20241064"
    }
  },
  {
    "ID": "Netclan20241065",
    "URL": "https://insights.blackcoffer.com/analytical-solution-for-a-tech-firm/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -7,
      "polarity_score": 0.5483869198751872,
      "subjectivity_score": 0.07808564035048765,
      "avg_sentence_length": 397.0,
      "percentage_complex_words": 52.64483627204031,
      "fog_index": 179.85793450881613,
      "complex_word_count": 209,
      "word_count": 397,
      "syllables_per_word": 3.118387909319899,
      "personal_pronouns": 0,
      "avg_word_length": 7.9672544080604535,
      "url_id": "Netclan20241065"
    }
  },
  {
    "ID": "Netclan20241066",
    "URL": "https://insights.blackcoffer.com/ai-solution-for-a-technology-information-and-internet-firm/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -2,
      "polarity_score": 0.8333329861112558,
      "subjectivity_score": 0.06315789307479229,
      "avg_sentence_length": 380.0,
      "percentage_complex_words": 55.52631578947368,
      "fog_index": 174.21052631578948,
      "complex_word_count": 211,
      "word_count": 380,
      "syllables_per_word": 3.2421052631578946,
      "personal_pronouns": 0,
      "avg_word_length": 8.102631578947369,
      "url_id": "Netclan20241066"
    }
  },
  {
    "ID": "Netclan20241067",
    "URL": "https://insights.blackcoffer.com/ai-and-nlp-based-solutions-to-automate-data-discovery-for-venture-capital-and-private-equity-principals/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -5,
      "polarity_score": 0.6296293964335569,
      "subjectivity_score": 0.05018587267312505,
      "avg_sentence_length": 538.0,
      "percentage_complex_words": 53.3457249070632,
      "fog_index": 236.53828996282527,
      "complex_word_count": 287,
      "word_count": 538,
      "syllables_per_word": 2.9814126394052045,
      "personal_pronouns": 0,
      "avg_word_length": 7.661710037174721,
      "url_id": "Netclan20241067"
    }
  },
  {
    "ID": "Netclan20241068",
    "URL": "https://insights.blackcoffer.com/an-etl-solution-for-an-internet-publishing-firm/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -7,
      "polarity_score": 0.5757574012856359,
      "subjectivity_score": 0.06547618917705975,
      "avg_sentence_length": 504.0,
      "percentage_complex_words": 47.817460317460316,
      "fog_index": 220.72698412698415,
      "complex_word_count": 241,
      "word_count": 504,
      "syllables_per_word": 2.888888888888889,
      "personal_pronouns": 0,
      "avg_word_length": 7.527777777777778,
      "url_id": "Netclan20241068"
    }
  },
  {
    "ID": "Netclan20241069",
    "URL": "https://insights.blackcoffer.com/ai-based-algorithmic-trading-bot-for-forex/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -8,
      "polarity_score": 0.40740725651583093,
      "subjectivity_score": 0.053571427508503425,
      "avg_sentence_length": 504.0,
      "percentage_complex_words": 48.01587301587302,
      "fog_index": 220.8063492063492,
      "complex_word_count": 242,
      "word_count": 504,
      "syllables_per_word": 2.876984126984127,
      "personal_pronouns": 0,
      "avg_word_length": 7.436507936507937,
      "url_id": "Netclan20241069"
    }
  },
  {
    "ID": "Netclan20241070",
    "URL": "https://insights.blackcoffer.com/equity-waterfalls-model-based-saas-application-for-real-estate-sector/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -4,
      "polarity_score": 0.6799997280001088,
      "subjectivity_score": 0.05760368530867085,
      "avg_sentence_length": 434.0,
      "percentage_complex_words": 56.91244239631337,
      "fog_index": 196.36497695852538,
      "complex_word_count": 247,
      "word_count": 434,
      "syllables_per_word": 3.1497695852534564,
      "personal_pronouns": 0,
      "avg_word_length": 7.928571428571429,
      "url_id": "Netclan20241070"
    }
  },
  {
    "ID": "Netclan20241071",
    "URL": "https://insights.blackcoffer.com/ai-solutions-for-foreign-exchange-an-automated-algo-trading-tool/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -2,
      "polarity_score": 0.8333329861112558,
      "subjectivity_score": 0.05309734395802337,
      "avg_sentence_length": 452.0,
      "percentage_complex_words": 51.76991150442478,
      "fog_index": 201.5079646017699,
      "complex_word_count": 234,
      "word_count": 452,
      "syllables_per_word": 3.061946902654867,
      "personal_pronouns": 0,
      "avg_word_length": 7.893805309734513,
      "url_id": "Netclan20241071"
    }
  },
  {
    "ID": "Netclan20241072",
    "URL": "https://insights.blackcoffer.com/ai-agent-development-and-deployment-in-jina-ai/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -5,
      "polarity_score": 0.6666664444445185,
      "subjectivity_score": 0.07853402935774793,
      "avg_sentence_length": 382.0,
      "percentage_complex_words": 57.32984293193717,
      "fog_index": 175.73193717277488,
      "complex_word_count": 219,
      "word_count": 382,
      "syllables_per_word": 3.274869109947644,
      "personal_pronouns": 0,
      "avg_word_length": 8.206806282722512,
      "url_id": "Netclan20241072"
    }
  },
  {
    "ID": "Netclan20241073",
    "URL": "https://insights.blackcoffer.com/golden-record-a-knowledge-graph-database-approach-to-unfold-discovery-using-neo4j/",
    "Analysis": {
      "positive_score": 30,
      "negative_score": -6,
      "polarity_score": 0.6666664814815328,
      "subjectivity_score": 0.07929515243843277,
      "avg_sentence_length": 454.0,
      "percentage_complex_words": 50.66079295154186,
      "fog_index": 201.86431718061675,
      "complex_word_count": 230,
      "word_count": 454,
      "syllables_per_word": 3.041850220264317,
      "personal_pronouns": 0,
      "avg_word_length": 7.817180616740088,
      "url_id": "Netclan20241073"
    }
  },
  {
    "ID": "Netclan20241074",
    "URL": "https://insights.blackcoffer.com/advanced-ai-for-trading-automation/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -2,
      "polarity_score": 0.8461535207101843,
      "subjectivity_score": 0.062350118408870066,
      "avg_sentence_length": 417.0,
      "percentage_complex_words": 52.99760191846523,
      "fog_index": 187.9990407673861,
      "complex_word_count": 221,
      "word_count": 417,
      "syllables_per_word": 3.160671462829736,
      "personal_pronouns": 0,
      "avg_word_length": 7.863309352517986,
      "url_id": "Netclan20241074"
    }
  },
  {
    "ID": "Netclan20241075",
    "URL": "https://insights.blackcoffer.com/create-a-knowledge-graph-to-provide-real-time-analytics-recommendations-and-a-single-source-of-truth/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -5,
      "polarity_score": 0.599999760000096,
      "subjectivity_score": 0.07002800924291291,
      "avg_sentence_length": 357.0,
      "percentage_complex_words": 54.061624649859944,
      "fog_index": 164.424649859944,
      "complex_word_count": 193,
      "word_count": 357,
      "syllables_per_word": 3.1736694677871147,
      "personal_pronouns": 0,
      "avg_word_length": 8.044817927170868,
      "url_id": "Netclan20241075"
    }
  },
  {
    "ID": "Netclan20241076",
    "URL": "https://insights.blackcoffer.com/advanced-ai-for-thermal-person-detection/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -2,
      "polarity_score": 0.8181814462811607,
      "subjectivity_score": 0.06940062872553222,
      "avg_sentence_length": 317.0,
      "percentage_complex_words": 54.25867507886435,
      "fog_index": 148.50347003154576,
      "complex_word_count": 172,
      "word_count": 317,
      "syllables_per_word": 3.2649842271293377,
      "personal_pronouns": 0,
      "avg_word_length": 8.249211356466876,
      "url_id": "Netclan20241076"
    }
  },
  {
    "ID": "Netclan20241077",
    "URL": "https://insights.blackcoffer.com/advanced-ai-for-road-cam-threat-detection/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -9,
      "polarity_score": 0.37931021403096066,
      "subjectivity_score": 0.08529411513840839,
      "avg_sentence_length": 340.0,
      "percentage_complex_words": 54.41176470588235,
      "fog_index": 157.76470588235293,
      "complex_word_count": 185,
      "word_count": 340,
      "syllables_per_word": 3.2794117647058822,
      "personal_pronouns": 0,
      "avg_word_length": 8.264705882352942,
      "url_id": "Netclan20241077"
    }
  },
  {
    "ID": "Netclan20241078",
    "URL": "https://insights.blackcoffer.com/advanced-ai-for-pedestrian-crossing-safety/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -3,
      "polarity_score": 0.7499996875001302,
      "subjectivity_score": 0.06722688887319639,
      "avg_sentence_length": 357.0,
      "percentage_complex_words": 54.34173669467787,
      "fog_index": 164.53669467787117,
      "complex_word_count": 194,
      "word_count": 357,
      "syllables_per_word": 3.2324929971988796,
      "personal_pronouns": 0,
      "avg_word_length": 8.201680672268907,
      "url_id": "Netclan20241078"
    }
  },
  {
    "ID": "Netclan20241079",
    "URL": "https://insights.blackcoffer.com/handgun-detection-using-yolo/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -2,
      "polarity_score": 0.8333329861112558,
      "subjectivity_score": 0.07339449316836413,
      "avg_sentence_length": 327.0,
      "percentage_complex_words": 57.18654434250765,
      "fog_index": 153.67461773700308,
      "complex_word_count": 187,
      "word_count": 327,
      "syllables_per_word": 3.36085626911315,
      "personal_pronouns": 0,
      "avg_word_length": 8.415902140672783,
      "url_id": "Netclan20241079"
    }
  },
  {
    "ID": "Netclan20241080",
    "URL": "https://insights.blackcoffer.com/using-graph-technology-to-create-single-customer-view/",
    "Analysis": {
      "positive_score": 18,
      "negative_score": -9,
      "polarity_score": 0.33333320987658893,
      "subjectivity_score": 0.07458563329873942,
      "avg_sentence_length": 362.0,
      "percentage_complex_words": 56.353591160220994,
      "fog_index": 167.34143646408842,
      "complex_word_count": 204,
      "word_count": 362,
      "syllables_per_word": 3.2375690607734806,
      "personal_pronouns": 0,
      "avg_word_length": 8.265193370165745,
      "url_id": "Netclan20241080"
    }
  },
  {
    "ID": "Netclan20241081",
    "URL": "https://insights.blackcoffer.com/car-detection-in-satellite-images/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -1,
      "polarity_score": 0.9259255829905249,
      "subjectivity_score": 0.06323184863625647,
      "avg_sentence_length": 427.0,
      "percentage_complex_words": 54.80093676814989,
      "fog_index": 192.72037470725996,
      "complex_word_count": 234,
      "word_count": 427,
      "syllables_per_word": 3.1124121779859486,
      "personal_pronouns": 0,
      "avg_word_length": 7.946135831381733,
      "url_id": "Netclan20241081"
    }
  },
  {
    "ID": "Netclan20241082",
    "URL": "https://insights.blackcoffer.com/building-a-physics-informed-neural-network-for-circuit-evaluation/",
    "Analysis": {
      "positive_score": 27,
      "negative_score": -4,
      "polarity_score": 0.7419352445370179,
      "subjectivity_score": 0.06709956564719555,
      "avg_sentence_length": 462.0,
      "percentage_complex_words": 55.41125541125541,
      "fog_index": 206.96450216450216,
      "complex_word_count": 256,
      "word_count": 462,
      "syllables_per_word": 3.101731601731602,
      "personal_pronouns": 0,
      "avg_word_length": 7.906926406926407,
      "url_id": "Netclan20241082"
    }
  },
  {
    "ID": "Netclan20241083",
    "URL": "https://insights.blackcoffer.com/connecting-mongodb-database-to-power-bi-dashboard-dashboard-automation/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -8,
      "polarity_score": 0.4838708116545769,
      "subjectivity_score": 0.061386137398294315,
      "avg_sentence_length": 505.0,
      "percentage_complex_words": 51.68316831683168,
      "fog_index": 222.67326732673268,
      "complex_word_count": 261,
      "word_count": 505,
      "syllables_per_word": 2.988118811881188,
      "personal_pronouns": 0,
      "avg_word_length": 7.554455445544554,
      "url_id": "Netclan20241083"
    }
  },
  {
    "ID": "Netclan20241084",
    "URL": "https://insights.blackcoffer.com/data-transformation/",
    "Analysis": {
      "positive_score": 33,
      "negative_score": -12,
      "polarity_score": 0.466666562962986,
      "subjectivity_score": 0.09018035891422127,
      "avg_sentence_length": 499.0,
      "percentage_complex_words": 48.69739478957916,
      "fog_index": 219.07895791583167,
      "complex_word_count": 243,
      "word_count": 499,
      "syllables_per_word": 2.8977955911823647,
      "personal_pronouns": 0,
      "avg_word_length": 7.5230460921843685,
      "url_id": "Netclan20241084"
    }
  },
  {
    "ID": "Netclan20241085",
    "URL": "https://insights.blackcoffer.com/e-commerce-store-analysis-purchase-behavior-ad-spend-conversion-traffic-etc/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -2,
      "polarity_score": 0.8399996640001344,
      "subjectivity_score": 0.055679286065049315,
      "avg_sentence_length": 449.0,
      "percentage_complex_words": 57.23830734966593,
      "fog_index": 202.49532293986638,
      "complex_word_count": 257,
      "word_count": 449,
      "syllables_per_word": 3.131403118040089,
      "personal_pronouns": 0,
      "avg_word_length": 7.879732739420936,
      "url_id": "Netclan20241085"
    }
  },
  
  {
    "ID": "Netclan20241086",
    "URL": "https://insights.blackcoffer.com/kpi-dashboard-for-accountants/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": 0,
      "polarity_score": 0.9999995454547521,
      "subjectivity_score": 0.05225653082526056,
      "avg_sentence_length": 421.0,
      "percentage_complex_words": 57.482185273159146,
      "fog_index": 191.39287410926366,
      "complex_word_count": 242,
      "word_count": 421,
      "syllables_per_word": 3.130641330166271,
      "personal_pronouns": 0,
      "avg_word_length": 7.990498812351544,
      "url_id": "Netclan20241086"
    }
  },
  {
    "ID": "Netclan20241087",
    "URL": "https://insights.blackcoffer.com/return-on-advertising-spend-dashboard-marketing-automation-and-analytics-using-etl-and-dashboard/",
    "Analysis": {
      "positive_score": 37,
      "negative_score": -6,
      "polarity_score": 0.7209300648999849,
      "subjectivity_score": 0.06466165316298267,
      "avg_sentence_length": 665.0,
      "percentage_complex_words": 58.796992481203006,
      "fog_index": 289.5187969924812,
      "complex_word_count": 391,
      "word_count": 665,
      "syllables_per_word": 3.1142857142857143,
      "personal_pronouns": 0,
      "avg_word_length": 7.980451127819549,
      "url_id": "Netclan20241087"
    }
  },
  {
    "ID": "Netclan20241088",
    "URL": "https://insights.blackcoffer.com/ranking-customer-behaviours-for-business-strategy/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -4,
      "polarity_score": 0.6923074260356054,
      "subjectivity_score": 0.06356968059731832,
      "avg_sentence_length": 409.0,
      "percentage_complex_words": 49.38875305623472,
      "fog_index": 183.3555012224939,
      "complex_word_count": 202,
      "word_count": 409,
      "syllables_per_word": 3.056234718826406,
      "personal_pronouns": 0,
      "avg_word_length": 7.919315403422983,
      "url_id": "Netclan20241088"
    }
  },
  {
    "ID": "Netclan20241089",
    "URL": "https://insights.blackcoffer.com/algorithmic-trading-for-multiple-commodities-markets-like-forex-metals-energy-etc/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": 0,
      "polarity_score": 0.9999995000002501,
      "subjectivity_score": 0.04901960664167631,
      "avg_sentence_length": 408.0,
      "percentage_complex_words": 56.86274509803921,
      "fog_index": 185.9450980392157,
      "complex_word_count": 232,
      "word_count": 408,
      "syllables_per_word": 3.218137254901961,
      "personal_pronouns": 0,
      "avg_word_length": 8.213235294117647,
      "url_id": "Netclan20241089"
    }
  },
  {
    "ID": "Netclan20241090",
    "URL": "https://insights.blackcoffer.com/trading-bot-for-forex/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": 2,
      "polarity_score": 0.7894732686982796,
      "subjectivity_score": 0.054755041649710616,
      "avg_sentence_length": 347.0,
      "percentage_complex_words": 49.56772334293948,
      "fog_index": 158.6270893371758,
      "complex_word_count": 172,
      "word_count": 347,
      "syllables_per_word": 3.152737752161383,
      "personal_pronouns": 0,
      "avg_word_length": 7.985590778097983,
      "url_id": "Netclan20241090"
    }
  },
  {
    "ID": "Netclan20241091",
    "URL": "https://insights.blackcoffer.com/python-model-for-the-analysis-of-sector-specific-stock-etfs-for-investment-purposes%ef%bf%bc/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -2,
      "polarity_score": 0.8333329861112558,
      "subjectivity_score": 0.05529953789632402,
      "avg_sentence_length": 434.0,
      "percentage_complex_words": 52.995391705069125,
      "fog_index": 194.79815668202764,
      "complex_word_count": 230,
      "word_count": 434,
      "syllables_per_word": 3.064516129032258,
      "personal_pronouns": 0,
      "avg_word_length": 7.921658986175115,
      "url_id": "Netclan20241091"
    }
  },
  {
    "ID": "Netclan20241092",
    "URL": "https://insights.blackcoffer.com/medical-classification/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -2,
      "polarity_score": 0.8095234240364647,
      "subjectivity_score": 0.04646017596327045,
      "avg_sentence_length": 452.0,
      "percentage_complex_words": 52.876106194690266,
      "fog_index": 201.9504424778761,
      "complex_word_count": 239,
      "word_count": 452,
      "syllables_per_word": 3.0265486725663715,
      "personal_pronouns": 0,
      "avg_word_length": 7.685840707964601,
      "url_id": "Netclan20241092"
    }
  },
  {
    "ID": "Netclan20241093",
    "URL": "https://insights.blackcoffer.com/design-develop-bert-question-answering-model-explanations-with-visualization/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": -5,
      "polarity_score": 0.5454542975207739,
      "subjectivity_score": 0.05152224703694972,
      "avg_sentence_length": 427.0,
      "percentage_complex_words": 52.92740046838408,
      "fog_index": 191.97096018735363,
      "complex_word_count": 226,
      "word_count": 427,
      "syllables_per_word": 3.1030444964871196,
      "personal_pronouns": 0,
      "avg_word_length": 7.885245901639344,
      "url_id": "Netclan20241093"
    }
  },
  {
    "ID": "Netclan20241094",
    "URL": "https://insights.blackcoffer.com/design-and-develop-solution-to-anomaly-detection-classification-problems/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -16,
      "polarity_score": 0.1351350986121355,
      "subjectivity_score": 0.08830548715261367,
      "avg_sentence_length": 419.0,
      "percentage_complex_words": 58.233890214797135,
      "fog_index": 190.89355608591887,
      "complex_word_count": 244,
      "word_count": 419,
      "syllables_per_word": 3.2553699284009547,
      "personal_pronouns": 0,
      "avg_word_length": 8.014319809069212,
      "url_id": "Netclan20241094"
    }
  },
  {
    "ID": "Netclan20241095",
    "URL": "https://insights.blackcoffer.com/an-etl-solution-for-currency-data-to-google-big-query/",
    "Analysis": {
      "positive_score": 16,
      "negative_score": -15,
      "polarity_score": 0.03225805411030513,
      "subjectivity_score": 0.06843266957102274,
      "avg_sentence_length": 453.0,
      "percentage_complex_words": 52.317880794701985,
      "fog_index": 202.1271523178808,
      "complex_word_count": 237,
      "word_count": 453,
      "syllables_per_word": 3.052980132450331,
      "personal_pronouns": 0,
      "avg_word_length": 7.664459161147903,
      "url_id": "Netclan20241095"
    }
  },
  {
    "ID": "Netclan20241096",
    "URL": "https://insights.blackcoffer.com/etl-and-mlops-infrastructure-for-blockchain-analytics/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -3,
      "polarity_score": 0.7272723966943652,
      "subjectivity_score": 0.04417670594022679,
      "avg_sentence_length": 498.0,
      "percentage_complex_words": 51.40562248995983,
      "fog_index": 219.76224899598392,
      "complex_word_count": 256,
      "word_count": 498,
      "syllables_per_word": 2.9196787148594376,
      "personal_pronouns": 0,
      "avg_word_length": 7.728915662650603,
      "url_id": "Netclan20241096"
    }
  },
  {
    "ID": "Netclan20241097",
    "URL": "https://insights.blackcoffer.com/an-agent-based-model-of-a-virtual-power-plant-vpp/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": -5,
      "polarity_score": 0.5454542975207739,
      "subjectivity_score": 0.04751619767783591,
      "avg_sentence_length": 463.0,
      "percentage_complex_words": 52.69978401727862,
      "fog_index": 206.27991360691146,
      "complex_word_count": 244,
      "word_count": 463,
      "syllables_per_word": 3.0280777537796975,
      "personal_pronouns": 0,
      "avg_word_length": 7.8034557235421165,
      "url_id": "Netclan20241097"
    }
  },
  {
    "ID": "Netclan20241098",
    "URL": "https://insights.blackcoffer.com/transform-api-into-sdk-library-and-widget/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -3,
      "polarity_score": 0.7599996960001216,
      "subjectivity_score": 0.06944444251543215,
      "avg_sentence_length": 360.0,
      "percentage_complex_words": 54.166666666666664,
      "fog_index": 165.66666666666669,
      "complex_word_count": 195,
      "word_count": 360,
      "syllables_per_word": 3.186111111111111,
      "personal_pronouns": 0,
      "avg_word_length": 8.188888888888888,
      "url_id": "Netclan20241098"
    }
  },
  {
    "ID": "Netclan20241099",
    "URL": "https://insights.blackcoffer.com/integration-of-a-product-to-a-cloud-based-crm-platform/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -6,
      "polarity_score": 0.5555553497943149,
      "subjectivity_score": 0.06617646896626302,
      "avg_sentence_length": 408.0,
      "percentage_complex_words": 52.69607843137255,
      "fog_index": 184.27843137254902,
      "complex_word_count": 215,
      "word_count": 408,
      "syllables_per_word": 3.0980392156862746,
      "personal_pronouns": 0,
      "avg_word_length": 7.997549019607843,
      "url_id": "Netclan20241099"
    }
  },
  {
    "ID": "Netclan20241100",
    "URL": "https://insights.blackcoffer.com/a-web-based-dashboard-for-the-filtered-data-retrieval-of-land-records/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -4,
      "polarity_score": 0.724137681331834,
      "subjectivity_score": 0.06791568927597917,
      "avg_sentence_length": 427.0,
      "percentage_complex_words": 52.459016393442624,
      "fog_index": 191.78360655737708,
      "complex_word_count": 224,
      "word_count": 427,
      "syllables_per_word": 3.098360655737705,
      "personal_pronouns": 0,
      "avg_word_length": 7.8969555035128804,
      "url_id": "Netclan20241100"
    }
  },
  {
    "ID": "Netclan20241101",
    "URL": "https://insights.blackcoffer.com/integration-of-video-conferencing-data-to-the-existing-web-app/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": -2,
      "polarity_score": 0.7894732686982796,
      "subjectivity_score": 0.04859334914083507,
      "avg_sentence_length": 391.0,
      "percentage_complex_words": 50.89514066496164,
      "fog_index": 176.75805626598466,
      "complex_word_count": 199,
      "word_count": 391,
      "syllables_per_word": 3.1074168797953963,
      "personal_pronouns": 0,
      "avg_word_length": 7.861892583120205,
      "url_id": "Netclan20241101"
    }
  },
  {
    "ID": "Netclan20241102",
    "URL": "https://insights.blackcoffer.com/design-develop-an-app-in-retool-which-shows-the-progress-of-the-added-video/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": 0,
      "polarity_score": 0.99999960000016,
      "subjectivity_score": 0.06561679617803685,
      "avg_sentence_length": 381.0,
      "percentage_complex_words": 51.96850393700787,
      "fog_index": 173.18740157480318,
      "complex_word_count": 198,
      "word_count": 381,
      "syllables_per_word": 3.1023622047244093,
      "personal_pronouns": 0,
      "avg_word_length": 7.850393700787402,
      "url_id": "Netclan20241102"
    }
  },
  {
    "ID": "Netclan20241103",
    "URL": "https://insights.blackcoffer.com/auvik-connectwise-integration-in-grafana/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -3,
      "polarity_score": 0.7391301134216899,
      "subjectivity_score": 0.059740258188564724,
      "avg_sentence_length": 385.0,
      "percentage_complex_words": 57.14285714285714,
      "fog_index": 176.85714285714286,
      "complex_word_count": 220,
      "word_count": 385,
      "syllables_per_word": 3.2493506493506494,
      "personal_pronouns": 0,
      "avg_word_length": 8.31948051948052,
      "url_id": "Netclan20241103"
    }
  },
  {
    "ID": "Netclan20241104",
    "URL": "https://insights.blackcoffer.com/data-integration-and-big-data-performance-using-elk-stack/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": 1,
      "polarity_score": 0.9090904958679564,
      "subjectivity_score": 0.051282050086665504,
      "avg_sentence_length": 429.0,
      "percentage_complex_words": 53.379953379953385,
      "fog_index": 192.95198135198137,
      "complex_word_count": 229,
      "word_count": 429,
      "syllables_per_word": 3.282051282051282,
      "personal_pronouns": 0,
      "avg_word_length": 8.363636363636363,
      "url_id": "Netclan20241104"
    }
  },
  {
    "ID": "Netclan20241105",
    "URL": "https://insights.blackcoffer.com/web-data-connector/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -1,
      "polarity_score": 0.899999550000225,
      "subjectivity_score": 0.04454342885203945,
      "avg_sentence_length": 449.0,
      "percentage_complex_words": 49.88864142538976,
      "fog_index": 199.5554565701559,
      "complex_word_count": 224,
      "word_count": 449,
      "syllables_per_word": 3.0534521158129175,
      "personal_pronouns": 0,
      "avg_word_length": 7.810690423162583,
      "url_id": "Netclan20241105"
    }
  },
  {
    "ID": "Netclan20241106",
    "URL": "https://insights.blackcoffer.com/an-app-for-updating-the-email-id-of-the-user-and-stripe-refund-tool-using-retool/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -1,
      "polarity_score": 0.9199996320001472,
      "subjectivity_score": 0.05938242139234154,
      "avg_sentence_length": 421.0,
      "percentage_complex_words": 56.294536817102134,
      "fog_index": 190.91781472684087,
      "complex_word_count": 237,
      "word_count": 421,
      "syllables_per_word": 3.0973871733966747,
      "personal_pronouns": 0,
      "avg_word_length": 7.707838479809976,
      "url_id": "Netclan20241106"
    }
  },

  {
    "ID": "Netclan20241107",
    "URL": "https://insights.blackcoffer.com/an-ai-ml-based-web-application-that-detects-the-correctness-of-text-in-a-given-video/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -7,
      "polarity_score": 0.4615382840237369,
      "subjectivity_score": 0.05922551117937332,
      "avg_sentence_length": 439.0,
      "percentage_complex_words": 50.79726651480638,
      "fog_index": 195.91890660592256,
      "complex_word_count": 223,
      "word_count": 439,
      "syllables_per_word": 3.052391799544419,
      "personal_pronouns": 0,
      "avg_word_length": 7.890660592255125,
      "url_id": "Netclan20241107"
    }
  },
  {
    "ID": "Netclan20241108",
    "URL": "https://insights.blackcoffer.com/website-tracking-and-insights-using-google-analytics-google-tag-manager/",
    "Analysis": {
      "positive_score": 35,
      "negative_score": -3,
      "polarity_score": 0.8421050415513048,
      "subjectivity_score": 0.05588235211937718,
      "avg_sentence_length": 680.0,
      "percentage_complex_words": 56.029411764705884,
      "fog_index": 294.4117647058824,
      "complex_word_count": 381,
      "word_count": 680,
      "syllables_per_word": 2.9411764705882355,
      "personal_pronouns": 0,
      "avg_word_length": 7.5588235294117645,
      "url_id": "Netclan20241108"
    }
  },
  {
    "ID": "Netclan20241109",
    "URL": "https://insights.blackcoffer.com/dashboard-to-track-the-analytics-of-the-website-using-google-analytics-and-google-tag-manager/",
    "Analysis": {
      "positive_score": 41,
      "negative_score": -2,
      "polarity_score": 0.9069765332612713,
      "subjectivity_score": 0.059310344009512496,
      "avg_sentence_length": 725.0,
      "percentage_complex_words": 55.03448275862068,
      "fog_index": 312.0137931034483,
      "complex_word_count": 399,
      "word_count": 725,
      "syllables_per_word": 2.9627586206896552,
      "personal_pronouns": 0,
      "avg_word_length": 7.5793103448275865,
      "url_id": "Netclan20241109"
    }
  },
  {
    "ID": "Netclan20241110",
    "URL": "https://insights.blackcoffer.com/power-bi-dashboard-on-operations-transactions-and-marketing-embedding-the-dashboard-to-web-app/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -5,
      "polarity_score": 0.6153843786983159,
      "subjectivity_score": 0.06499999837500005,
      "avg_sentence_length": 400.0,
      "percentage_complex_words": 57.75,
      "fog_index": 183.10000000000002,
      "complex_word_count": 231,
      "word_count": 400,
      "syllables_per_word": 3.21,
      "personal_pronouns": 0,
      "avg_word_length": 8.0875,
      "url_id": "Netclan20241110"
    }
  },
  {
    "ID": "Netclan20241111",
    "URL": "https://insights.blackcoffer.com/nft-data-automation-looksrare-and-etl-tool/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -2,
      "polarity_score": 0.8333329861112558,
      "subjectivity_score": 0.05607476504498213,
      "avg_sentence_length": 428.0,
      "percentage_complex_words": 51.16822429906542,
      "fog_index": 191.66728971962618,
      "complex_word_count": 219,
      "word_count": 428,
      "syllables_per_word": 3.053738317757009,
      "personal_pronouns": 0,
      "avg_word_length": 7.6985981308411215,
      "url_id": "Netclan20241111"
    }
  },
    {
    "ID": "Netclan20241112",
    "URL": "https://insights.blackcoffer.com/optimize-the-data-scraper-program-to-easily-accommodate-large-files-and-solve-oom-errors/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -4,
      "polarity_score": 0.7037034430727989,
      "subjectivity_score": 0.07049608171028508,
      "avg_sentence_length": 383.0,
      "percentage_complex_words": 52.48041775456919,
      "fog_index": 174.1921671018277,
      "complex_word_count": 201,
      "word_count": 383,
      "syllables_per_word": 3.1592689295039165,
      "personal_pronouns": 0,
      "avg_word_length": 7.994778067885117,
      "url_id": "Netclan20241112"
    }
  },
  {
    "ID": "Netclan20241113",
    "URL": "https://insights.blackcoffer.com/making-a-robust-way-to-sync-data-from-airtables-to-mongodb-using-python-etl-solution/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -6,
      "polarity_score": 0.5555553497943149,
      "subjectivity_score": 0.06150341545550307,
      "avg_sentence_length": 439.0,
      "percentage_complex_words": 50.56947608200456,
      "fog_index": 195.82779043280183,
      "complex_word_count": 222,
      "word_count": 439,
      "syllables_per_word": 3.1161731207289294,
      "personal_pronouns": 0,
      "avg_word_length": 7.899772209567198,
      "url_id": "Netclan20241113"
    }
  },
  {
    "ID": "Netclan20241114",
    "URL": "https://insights.blackcoffer.com/incident-duration-prediction-infrastructure-and-real-estate/",
    "Analysis": {
      "positive_score": 18,
      "negative_score": 0,
      "polarity_score": 0.9999994444447531,
      "subjectivity_score": 0.04812834095913527,
      "avg_sentence_length": 374.0,
      "percentage_complex_words": 59.62566844919787,
      "fog_index": 173.45026737967916,
      "complex_word_count": 223,
      "word_count": 374,
      "syllables_per_word": 3.328877005347594,
      "personal_pronouns": 0,
      "avg_word_length": 8.481283422459892,
      "url_id": "Netclan20241114"
    }
  },
  {
    "ID": "Netclan20241115",
    "URL": "https://insights.blackcoffer.com/statistical-data-analysis-of-reinforced-concrete/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -4,
      "polarity_score": 0.7142854591837646,
      "subjectivity_score": 0.059196616084638144,
      "avg_sentence_length": 473.0,
      "percentage_complex_words": 58.350951374207185,
      "fog_index": 212.54038054968288,
      "complex_word_count": 276,
      "word_count": 473,
      "syllables_per_word": 3.236786469344609,
      "personal_pronouns": 0,
      "avg_word_length": 8.232558139534884,
      "url_id": "Netclan20241115"
    }
  },
  {
    "ID": "Netclan20241116",
    "URL": "https://insights.blackcoffer.com/database-normalization-segmentation-with-google-data-studio-dashboard-insights/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -1,
      "polarity_score": 0.9047614739231077,
      "subjectivity_score": 0.05497382055042355,
      "avg_sentence_length": 382.0,
      "percentage_complex_words": 55.75916230366492,
      "fog_index": 175.103664921466,
      "complex_word_count": 213,
      "word_count": 382,
      "syllables_per_word": 3.2146596858638743,
      "personal_pronouns": 0,
      "avg_word_length": 7.9319371727748695,
      "url_id": "Netclan20241116"
    }
  },
  {
    "ID": "Netclan20241117",
    "URL": "https://insights.blackcoffer.com/power-bi-dashboard-to-drive-insights-from-complex-data-to-generate-business-insights/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -5,
      "polarity_score": 0.6153843786983159,
      "subjectivity_score": 0.060185183792009635,
      "avg_sentence_length": 432.0,
      "percentage_complex_words": 51.85185185185185,
      "fog_index": 193.54074074074074,
      "complex_word_count": 224,
      "word_count": 432,
      "syllables_per_word": 3.0439814814814814,
      "personal_pronouns": 0,
      "avg_word_length": 7.722222222222222,
      "url_id": "Netclan20241117"
    }
  },
  {
    "ID": "Netclan20241118",
    "URL": "https://insights.blackcoffer.com/real-time-dashboard-to-monitor-infrastructure-activity-and-machines/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": -3,
      "polarity_score": 0.699999650000175,
      "subjectivity_score": 0.048661799302632626,
      "avg_sentence_length": 411.0,
      "percentage_complex_words": 58.3941605839416,
      "fog_index": 187.75766423357663,
      "complex_word_count": 240,
      "word_count": 411,
      "syllables_per_word": 3.2068126520681264,
      "personal_pronouns": 0,
      "avg_word_length": 8.221411192214111,
      "url_id": "Netclan20241118"
    }
  },
  {
    "ID": "Netclan20241119",
    "URL": "https://insights.blackcoffer.com/electric-vehicles-ev-load-management-system-to-forecast-energy-demand/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -7,
      "polarity_score": 0.4814813031550729,
      "subjectivity_score": 0.05613305496604876,
      "avg_sentence_length": 481.0,
      "percentage_complex_words": 54.469854469854475,
      "fog_index": 214.18794178794178,
      "complex_word_count": 262,
      "word_count": 481,
      "syllables_per_word": 3.103950103950104,
      "personal_pronouns": 0,
      "avg_word_length": 7.881496881496881,
      "url_id": "Netclan20241119"
    }
  },
  {
    "ID": "Netclan20241120",
    "URL": "https://insights.blackcoffer.com/power-bi-data-driven-map-dashboard/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -1,
      "polarity_score": 0.899999550000225,
      "subjectivity_score": 0.05263157756232691,
      "avg_sentence_length": 380.0,
      "percentage_complex_words": 52.89473684210526,
      "fog_index": 173.1578947368421,
      "complex_word_count": 201,
      "word_count": 380,
      "syllables_per_word": 3.142105263157895,
      "personal_pronouns": 0,
      "avg_word_length": 8.021052631578947,
      "url_id": "Netclan20241120"
    }
  },
  {
    "ID": "Netclan20241121",
    "URL": "https://insights.blackcoffer.com/google-local-service-ads-lsa-leads-dashboard/",
    "Analysis": {
      "positive_score": 47,
      "negative_score": -6,
      "polarity_score": 0.7735847597009887,
      "subjectivity_score": 0.07969924692181583,
      "avg_sentence_length": 665.0,
      "percentage_complex_words": 52.33082706766917,
      "fog_index": 286.9323308270677,
      "complex_word_count": 348,
      "word_count": 665,
      "syllables_per_word": 2.9368421052631577,
      "personal_pronouns": 0,
      "avg_word_length": 7.455639097744361,
      "url_id": "Netclan20241121"
    }
  },
  {
    "ID": "Netclan20241122",
    "URL": "https://insights.blackcoffer.com/aws-lex-voice-and-chatbot/",
    "Analysis": {
      "positive_score": 29,
      "negative_score": -1,
      "polarity_score": 0.933333022222326,
      "subjectivity_score": 0.05882352825836219,
      "avg_sentence_length": 510.0,
      "percentage_complex_words": 46.666666666666664,
      "fog_index": 222.66666666666666,
      "complex_word_count": 238,
      "word_count": 510,
      "syllables_per_word": 2.8137254901960786,
      "personal_pronouns": 0,
      "avg_word_length": 7.2254901960784315,
      "url_id": "Netclan20241122"
    }
  },
  {
    "ID": "Netclan20241123",
    "URL": "https://insights.blackcoffer.com/metabridges-api-decentraland-integration/",
    "Analysis": {
      "positive_score": 18,
      "negative_score": -5,
      "polarity_score": 0.5652171455577628,
      "subjectivity_score": 0.05808080661412105,
      "avg_sentence_length": 396.0,
      "percentage_complex_words": 53.03030303030303,
      "fog_index": 179.61212121212122,
      "complex_word_count": 210,
      "word_count": 396,
      "syllables_per_word": 3.0984848484848486,
      "personal_pronouns": 0,
      "avg_word_length": 7.861111111111111,
      "url_id": "Netclan20241123"
    }
  },
  {
    "ID": "Netclan20241124",
    "URL": "https://insights.blackcoffer.com/microsoft-azure-chatbot-with-luis-language-understanding/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -1,
      "polarity_score": 0.9090904958679564,
      "subjectivity_score": 0.054187190783566735,
      "avg_sentence_length": 406.0,
      "percentage_complex_words": 58.620689655172406,
      "fog_index": 185.84827586206896,
      "complex_word_count": 238,
      "word_count": 406,
      "syllables_per_word": 3.2192118226600983,
      "personal_pronouns": 0,
      "avg_word_length": 8.113300492610838,
      "url_id": "Netclan20241124"
    }
  },
  {
    "ID": "Netclan20241125",
    "URL": "https://insights.blackcoffer.com/impact-of-news-media-and-press-on-innovation-startups-and-investments/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -4,
      "polarity_score": 0.7333330888889704,
      "subjectivity_score": 0.07672634074868694,
      "avg_sentence_length": 391.0,
      "percentage_complex_words": 55.754475703324815,
      "fog_index": 178.70179028132995,
      "complex_word_count": 218,
      "word_count": 391,
      "syllables_per_word": 3.1815856777493607,
      "personal_pronouns": 0,
      "avg_word_length": 7.9258312020460355,
      "url_id": "Netclan20241125"
    }
  },
  {
    "ID": "Netclan20241126",
    "URL": "https://insights.blackcoffer.com/aws-quicksight-reporting-dashboard/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -3,
      "polarity_score": 0.7931031747920088,
      "subjectivity_score": 0.05719920991717535,
      "avg_sentence_length": 507.0,
      "percentage_complex_words": 50.887573964497044,
      "fog_index": 223.15502958579884,
      "complex_word_count": 258,
      "word_count": 507,
      "syllables_per_word": 2.992110453648915,
      "personal_pronouns": 0,
      "avg_word_length": 7.777120315581854,
      "url_id": "Netclan20241126"
    }
  },
  {
    "ID": "Netclan20241127",
    "URL": "https://insights.blackcoffer.com/google-data-studio-dashboard-for-marketing-ads-and-traction-data/",
    "Analysis": {
      "positive_score": 26,
      "negative_score": -4,
      "polarity_score": 0.7333330888889704,
      "subjectivity_score": 0.05859374885559084,
      "avg_sentence_length": 512.0,
      "percentage_complex_words": 51.953125,
      "fog_index": 225.58125,
      "complex_word_count": 266,
      "word_count": 512,
      "syllables_per_word": 2.986328125,
      "personal_pronouns": 0,
      "avg_word_length": 7.611328125,
      "url_id": "Netclan20241127"
    }
  },
  {
    "ID": "Netclan20241128",
    "URL": "https://insights.blackcoffer.com/gangala-in-e-commerce-big-data-etl-elt-solution-and-data-warehouse/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -3,
      "polarity_score": 0.7692304733728949,
      "subjectivity_score": 0.06132075327073695,
      "avg_sentence_length": 424.0,
      "percentage_complex_words": 51.41509433962265,
      "fog_index": 190.16603773584907,
      "complex_word_count": 218,
      "word_count": 424,
      "syllables_per_word": 3.0542452830188678,
      "personal_pronouns": 0,
      "avg_word_length": 7.7075471698113205,
      "url_id": "Netclan20241128"
    }
  },
  {
    "ID": "Netclan20241129",
    "URL": "https://insights.blackcoffer.com/big-data-solution-to-an-online-multivendor-marketplace-ecommerce-business/",
    "Analysis": {
      "positive_score": 36,
      "negative_score": -5,
      "polarity_score": 0.7560973765616155,
      "subjectivity_score": 0.07721280457226357,
      "avg_sentence_length": 531.0,
      "percentage_complex_words": 49.152542372881356,
      "fog_index": 232.06101694915256,
      "complex_word_count": 261,
      "word_count": 531,
      "syllables_per_word": 3.0094161958568737,
      "personal_pronouns": 0,
      "avg_word_length": 7.645951035781544,
      "url_id": "Netclan20241129"
    }
  },
  {
    "ID": "Netclan20241130",
    "URL": "https://insights.blackcoffer.com/creating-a-custom-report-and-dashboard-using-the-data-got-from-atera-api/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": -4,
      "polarity_score": 0.619047324263179,
      "subjectivity_score": 0.05691056756339926,
      "avg_sentence_length": 369.0,
      "percentage_complex_words": 55.82655826558266,
      "fog_index": 169.9306233062331,
      "complex_word_count": 206,
      "word_count": 369,
      "syllables_per_word": 3.186991869918699,
      "personal_pronouns": 0,
      "avg_word_length": 8.032520325203253,
      "url_id": "Netclan20241130"
    }
  },
  {
    "ID": "Netclan20241131",
    "URL": "https://insights.blackcoffer.com/azure-data-lake-and-power-bi-dashboard/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -3,
      "polarity_score": 0.7499996875001302,
      "subjectivity_score": 0.056872036567013354,
      "avg_sentence_length": 422.0,
      "percentage_complex_words": 58.29383886255924,
      "fog_index": 192.1175355450237,
      "complex_word_count": 246,
      "word_count": 422,
      "syllables_per_word": 3.3364928909952605,
      "personal_pronouns": 0,
      "avg_word_length": 8.412322274881516,
      "url_id": "Netclan20241131"
    }
  },
  {
    "ID": "Netclan20241132",
    "URL": "https://insights.blackcoffer.com/google-data-studio-pipeline-with-gcp-mysql/",
    "Analysis": {
      "positive_score": 16,
      "negative_score": -10,
      "polarity_score": 0.23076914201186846,
      "subjectivity_score": 0.04377104303415753,
      "avg_sentence_length": 594.0,
      "percentage_complex_words": 47.97979797979798,
      "fog_index": 256.7919191919192,
      "complex_word_count": 285,
      "word_count": 594,
      "syllables_per_word": 2.846801346801347,
      "personal_pronouns": 0,
      "avg_word_length": 7.388888888888889,
      "url_id": "Netclan20241132"
    }
  },
  {
    "ID": "Netclan20241133",
    "URL": "https://insights.blackcoffer.com/quickbooks-dashboard-to-find-patterns-in-finance-sales-and-forecasts/",
    "Analysis": {
      "positive_score": 37,
      "negative_score": -13,
      "polarity_score": 0.4799999040000192,
      "subjectivity_score": 0.058548008682107626,
      "avg_sentence_length": 854.0,
      "percentage_complex_words": 53.74707259953162,
      "fog_index": 363.0988290398127,
      "complex_word_count": 459,
      "word_count": 854,
      "syllables_per_word": 3.003512880562061,
      "personal_pronouns": 0,
      "avg_word_length": 7.5796252927400465,
      "url_id": "Netclan20241133"
    }
  },
  {
    "ID": "Netclan20241134",
    "URL": "https://insights.blackcoffer.com/marketing-sales-and-financial-data-business-dashboard-wink-report/",
    "Analysis": {
      "positive_score": 25,
      "negative_score": -3,
      "polarity_score": 0.7857140051021411,
      "subjectivity_score": 0.04494381950330948,
      "avg_sentence_length": 623.0,
      "percentage_complex_words": 54.73515248796148,
      "fog_index": 271.09406099518463,
      "complex_word_count": 341,
      "word_count": 623,
      "syllables_per_word": 3.081861958266453,
      "personal_pronouns": 0,
      "avg_word_length": 7.959871589085072,
      "url_id": "Netclan20241134"
    }
  },
  {
    "ID": "Netclan20241135",
    "URL": "https://insights.blackcoffer.com/react-native-apps-in-the-development-portfolio/",
    "Analysis": {
      "positive_score": 16,
      "negative_score": -1,
      "polarity_score": 0.882352422145634,
      "subjectivity_score": 0.059649120714065945,
      "avg_sentence_length": 285.0,
      "percentage_complex_words": 55.43859649122807,
      "fog_index": 136.17543859649123,
      "complex_word_count": 158,
      "word_count": 285,
      "syllables_per_word": 3.245614035087719,
      "personal_pronouns": 0,
      "avg_word_length": 8.087719298245615,
      "url_id": "Netclan20241135"
    }
  },
  {
    "ID": "Netclan20241136",
    "URL": "https://insights.blackcoffer.com/a-leading-firm-website-seo-optimization/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": 0,
      "polarity_score": 0.9999995238097505,
      "subjectivity_score": 0.06140350697650565,
      "avg_sentence_length": 342.0,
      "percentage_complex_words": 58.77192982456141,
      "fog_index": 160.3087719298246,
      "complex_word_count": 201,
      "word_count": 342,
      "syllables_per_word": 3.3362573099415203,
      "personal_pronouns": 0,
      "avg_word_length": 8.301169590643275,
      "url_id": "Netclan20241136"
    }
  },
  {
    "ID": "Netclan20241137",
    "URL": "https://insights.blackcoffer.com/a-leading-hospitality-firm-in-the-usa-website-seo-optimization/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -1,
      "polarity_score": 0.9199996320001472,
      "subjectivity_score": 0.07507507282056838,
      "avg_sentence_length": 333.0,
      "percentage_complex_words": 57.35735735735735,
      "fog_index": 156.14294294294294,
      "complex_word_count": 191,
      "word_count": 333,
      "syllables_per_word": 3.27027027027027,
      "personal_pronouns": 0,
      "avg_word_length": 8.18018018018018,
      "url_id": "Netclan20241137"
    }
  },
  {
    "ID": "Netclan20241138",
    "URL": "https://insights.blackcoffer.com/a-leading-firm-in-the-usa-website-seo-optimization/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -4,
      "polarity_score": 0.7142854591837646,
      "subjectivity_score": 0.08588956791749792,
      "avg_sentence_length": 326.0,
      "percentage_complex_words": 56.74846625766872,
      "fog_index": 153.0993865030675,
      "complex_word_count": 185,
      "word_count": 326,
      "syllables_per_word": 3.315950920245399,
      "personal_pronouns": 0,
      "avg_word_length": 8.315950920245399,
      "url_id": "Netclan20241138"
    }
  },
  {
    "ID": "Netclan20241139",
    "URL": "https://insights.blackcoffer.com/a-leading-musical-instrumental-website-seo-optimization/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -2,
      "polarity_score": 0.8260865973536533,
      "subjectivity_score": 0.07165108811055801,
      "avg_sentence_length": 321.0,
      "percentage_complex_words": 58.25545171339564,
      "fog_index": 151.70218068535826,
      "complex_word_count": 187,
      "word_count": 321,
      "syllables_per_word": 3.308411214953271,
      "personal_pronouns": 0,
      "avg_word_length": 8.193146417445483,
      "url_id": "Netclan20241139"
    }
  },
  {
    "ID": "Netclan20241140",
    "URL": "https://insights.blackcoffer.com/a-leading-firm-in-the-usa-seo-and-website-optimization/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -1,
      "polarity_score": 0.9047614739231077,
      "subjectivity_score": 0.0658307189394759,
      "avg_sentence_length": 319.0,
      "percentage_complex_words": 57.68025078369906,
      "fog_index": 150.67210031347963,
      "complex_word_count": 184,
      "word_count": 319,
      "syllables_per_word": 3.341692789968652,
      "personal_pronouns": 0,
      "avg_word_length": 8.35423197492163,
      "url_id": "Netclan20241140"
    }
  },
  {
    "ID": "Netclan20241141",
    "URL": "https://insights.blackcoffer.com/immigration-datawarehouse-ai-based-recommendations/",
    "Analysis": {
      "positive_score": 29,
      "negative_score": -5,
      "polarity_score": 0.7058821453287807,
      "subjectivity_score": 0.06551059604025827,
      "avg_sentence_length": 519.0,
      "percentage_complex_words": 53.94990366088632,
      "fog_index": 229.17996146435453,
      "complex_word_count": 280,
      "word_count": 519,
      "syllables_per_word": 3.073217726396917,
      "personal_pronouns": 0,
      "avg_word_length": 7.857418111753372,
      "url_id": "Netclan20241141"
    }
  },
  {
    "ID": "Netclan20241142",
    "URL": "https://insights.blackcoffer.com/lipsync-automation-for-celebrities-and-influencers/",
    "Analysis": {
      "positive_score": 18,
      "negative_score": -1,
      "polarity_score": 0.8947363711913836,
      "subjectivity_score": 0.057926827502230875,
      "avg_sentence_length": 328.0,
      "percentage_complex_words": 59.756097560975604,
      "fog_index": 155.10243902439026,
      "complex_word_count": 196,
      "word_count": 328,
      "syllables_per_word": 3.4207317073170733,
      "personal_pronouns": 0,
      "avg_word_length": 8.359756097560975,
      "url_id": "Netclan20241142"
    }
  },
  {
    "ID": "Netclan20241143",
    "URL": "https://insights.blackcoffer.com/key-audit-matters-predictive-modeling/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -7,
      "polarity_score": 0.4814813031550729,
      "subjectivity_score": 0.05212355111730597,
      "avg_sentence_length": 518.0,
      "percentage_complex_words": 54.633204633204635,
      "fog_index": 229.05328185328187,
      "complex_word_count": 283,
      "word_count": 518,
      "syllables_per_word": 3.0791505791505793,
      "personal_pronouns": 0,
      "avg_word_length": 7.737451737451737,
      "url_id": "Netclan20241143"
    }
  },
  {
    "ID": "Netclan20241144",
    "URL": "https://insights.blackcoffer.com/splitting-of-songs-into-its-vocals-and-instrumental/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -4,
      "polarity_score": 0.7037034430727989,
      "subjectivity_score": 0.07317072972437047,
      "avg_sentence_length": 369.0,
      "percentage_complex_words": 52.30352303523035,
      "fog_index": 168.52140921409216,
      "complex_word_count": 193,
      "word_count": 369,
      "syllables_per_word": 3.16260162601626,
      "personal_pronouns": 0,
      "avg_word_length": 8.024390243902438,
      "url_id": "Netclan20241144"
    }
  },
  {
    "ID": "Netclan20241145",
    "URL": "https://insights.blackcoffer.com/ai-and-ml-technologies-to-evaluate-learning-assessments/",
    "Analysis": {
      "positive_score": 27,
      "negative_score": -3,
      "polarity_score": 0.7999997333334222,
      "subjectivity_score": 0.06849314912116099,
      "avg_sentence_length": 438.0,
      "percentage_complex_words": 56.62100456621004,
      "fog_index": 197.84840182648404,
      "complex_word_count": 248,
      "word_count": 438,
      "syllables_per_word": 3.180365296803653,
      "personal_pronouns": 0,
      "avg_word_length": 7.997716894977169,
      "url_id": "Netclan20241145"
    }
  },
  {
    "ID": "Netclan20241146",
    "URL": "https://insights.blackcoffer.com/datawarehouse-and-recommendations-engine-for-airbnb/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": -5,
      "polarity_score": 0.7222220216049939,
      "subjectivity_score": 0.07999999822222227,
      "avg_sentence_length": 450.0,
      "percentage_complex_words": 52.0,
      "fog_index": 200.8,
      "complex_word_count": 234,
      "word_count": 450,
      "syllables_per_word": 3.042222222222222,
      "personal_pronouns": 0,
      "avg_word_length": 7.851111111111111,
      "url_id": "Netclan20241146"
    }
  },
  {
    "ID": "Netclan20241147",
    "URL": "https://insights.blackcoffer.com/real-estate-data-warehouse/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": 0,
      "polarity_score": 0.9999995238097505,
      "subjectivity_score": 0.05289672410839486,
      "avg_sentence_length": 397.0,
      "percentage_complex_words": 52.896725440806044,
      "fog_index": 179.95869017632242,
      "complex_word_count": 210,
      "word_count": 397,
      "syllables_per_word": 3.158690176322418,
      "personal_pronouns": 0,
      "avg_word_length": 8.120906801007557,
      "url_id": "Netclan20241147"
    }
  },
  {
    "ID": "Netclan20241148",
    "URL": "https://insights.blackcoffer.com/traction-dashboards-of-marketing-campaigns-and-posts/",
    "Analysis": {
      "positive_score": 19,
      "negative_score": -2,
      "polarity_score": 0.8095234240364647,
      "subjectivity_score": 0.04988123396956689,
      "avg_sentence_length": 421.0,
      "percentage_complex_words": 53.20665083135392,
      "fog_index": 189.68266033254156,
      "complex_word_count": 224,
      "word_count": 421,
      "syllables_per_word": 3.0997624703087885,
      "personal_pronouns": 0,
      "avg_word_length": 7.933491686460807,
      "url_id": "Netclan20241148"
    }
  },
  {
    "ID": "Netclan20241149",
    "URL": "https://insights.blackcoffer.com/google-local-service-ads-lsa-data-warehouse/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -2,
      "polarity_score": 0.8181814462811607,
      "subjectivity_score": 0.055979642341484934,
      "avg_sentence_length": 393.0,
      "percentage_complex_words": 56.74300254452926,
      "fog_index": 179.8972010178117,
      "complex_word_count": 223,
      "word_count": 393,
      "syllables_per_word": 3.27735368956743,
      "personal_pronouns": 0,
      "avg_word_length": 8.099236641221374,
      "url_id": "Netclan20241149"
    }
  },
  {
    "ID": "Netclan20241150",
    "URL": "https://insights.blackcoffer.com/google-local-service-ads-missed-calls-and-messages-automation-tool/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -7,
      "polarity_score": 0.4814813031550729,
      "subjectivity_score": 0.06818181646005514,
      "avg_sentence_length": 396.0,
      "percentage_complex_words": 55.3030303030303,
      "fog_index": 180.52121212121213,
      "complex_word_count": 219,
      "word_count": 396,
      "syllables_per_word": 3.242424242424242,
      "personal_pronouns": 0,
      "avg_word_length": 8.128787878787879,
      "url_id": "Netclan20241150"
    }
  },
  {
    "ID": "Netclan20241151",
    "URL": "https://insights.blackcoffer.com/marketing-ads-leads-call-status-data-tool-to-bigquery/",
    "Analysis": {
      "positive_score": 21,
      "negative_score": -3,
      "polarity_score": 0.7499996875001302,
      "subjectivity_score": 0.0633245365877431,
      "avg_sentence_length": 379.0,
      "percentage_complex_words": 55.93667546174142,
      "fog_index": 173.97467018469658,
      "complex_word_count": 212,
      "word_count": 379,
      "syllables_per_word": 3.2770448548812663,
      "personal_pronouns": 0,
      "avg_word_length": 8.213720316622691,
      "url_id": "Netclan20241151"
    }
  },
  {
    "ID": "Netclan20241152",
    "URL": "https://insights.blackcoffer.com/marketing-analytics-to-automate-leads-call-status-and-reporting/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -3,
      "polarity_score": 0.7599996960001216,
      "subjectivity_score": 0.06281406877351586,
      "avg_sentence_length": 398.0,
      "percentage_complex_words": 56.03015075376885,
      "fog_index": 181.61206030150754,
      "complex_word_count": 223,
      "word_count": 398,
      "syllables_per_word": 3.2437185929648242,
      "personal_pronouns": 0,
      "avg_word_length": 8.163316582914574,
      "url_id": "Netclan20241152"
    }
  },
  {
    "ID": "Netclan20241153",
    "URL": "https://insights.blackcoffer.com/callrail-analytics-leads-report-alert/",
    "Analysis": {
      "positive_score": 22,
      "negative_score": -1,
      "polarity_score": 0.9130430812856168,
      "subjectivity_score": 0.06149732455889507,
      "avg_sentence_length": 374.0,
      "percentage_complex_words": 52.67379679144385,
      "fog_index": 170.66951871657756,
      "complex_word_count": 197,
      "word_count": 374,
      "syllables_per_word": 3.2032085561497325,
      "personal_pronouns": 0,
      "avg_word_length": 8.120320855614974,
      "url_id": "Netclan20241153"
    }
  },
  {
    "ID": "Netclan20241154",
    "URL": "https://insights.blackcoffer.com/marketing-automation-tool-to-notify-lead-details-to-clients-over-email-and-phone/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -2,
      "polarity_score": 0.8461535207101843,
      "subjectivity_score": 0.06701030755128073,
      "avg_sentence_length": 388.0,
      "percentage_complex_words": 54.123711340206185,
      "fog_index": 176.84948453608249,
      "complex_word_count": 210,
      "word_count": 388,
      "syllables_per_word": 3.1907216494845363,
      "personal_pronouns": 0,
      "avg_word_length": 8.007731958762887,
      "url_id": "Netclan20241154"
    }
  },
  {
    "ID": "Netclan20241155",
    "URL": "https://insights.blackcoffer.com/data-etl-local-service-ads-leads-to-bigquery/",
    "Analysis": {
      "positive_score": 23,
      "negative_score": -1,
      "polarity_score": 0.9166662847223814,
      "subjectivity_score": 0.06075949213267109,
      "avg_sentence_length": 395.0,
      "percentage_complex_words": 55.949367088607595,
      "fog_index": 180.37974683544303,
      "complex_word_count": 221,
      "word_count": 395,
      "syllables_per_word": 3.2734177215189875,
      "personal_pronouns": 0,
      "avg_word_length": 8.139240506329115,
      "url_id": "Netclan20241155"
    }
  },
  {
    "ID": "Netclan20241156",
    "URL": "https://insights.blackcoffer.com/marbles-stimulation-using-python/",
    "Analysis": {
      "positive_score": 31,
      "negative_score": -2,
      "polarity_score": 0.8787876124886022,
      "subjectivity_score": 0.07382550170412748,
      "avg_sentence_length": 447.0,
      "percentage_complex_words": 54.36241610738255,
      "fog_index": 200.54496644295304,
      "complex_word_count": 243,
      "word_count": 447,
      "syllables_per_word": 3.1364653243847873,
      "personal_pronouns": 0,
      "avg_word_length": 8.05592841163311,
      "url_id": "Netclan20241156"
    }
  },
  {
    "ID": "Netclan20241157",
    "URL": "https://insights.blackcoffer.com/stocktwit,s-data-structurization/",
    "Analysis": {
      "positive_score": 30,
      "negative_score": -9,
      "polarity_score": 0.5384614003945126,
      "subjectivity_score": 0.05416666591435186,
      "avg_sentence_length": 720.0,
      "percentage_complex_words": 44.44444444444444,
      "fog_index": 305.77777777777777,
      "complex_word_count": 320,
      "word_count": 720,
      "syllables_per_word": 2.825,
      "personal_pronouns": 0,
      "avg_word_length": 7.4375,
      "url_id": "Netclan20241157"
    }
  },
  {
    "ID": "Netclan20241158",
    "URL": "https://insights.blackcoffer.com/sentimental-analysis-on-shareholder-letter-of-companies/",
    "Analysis": {
      "positive_score": 20,
      "negative_score": -7,
      "polarity_score": 0.4814813031550729,
      "subjectivity_score": 0.05133079750321678,
      "avg_sentence_length": 526.0,
      "percentage_complex_words": 56.84410646387833,
      "fog_index": 233.13764258555136,
      "complex_word_count": 299,
      "word_count": 526,
      "syllables_per_word": 3.193916349809886,
      "personal_pronouns": 0,
      "avg_word_length": 8.230038022813687,
      "url_id": "Netclan20241158"
    }
  },
  {
    "ID": "Netclan20241159",
    "URL": "https://insights.blackcoffer.com/population-and-community-survey-of-america/",
    "Analysis": {
      "positive_score": 28,
      "negative_score": -6,
      "polarity_score": 0.647058633218049,
      "subjectivity_score": 0.048502139108386036,
      "avg_sentence_length": 701.0,
      "percentage_complex_words": 50.21398002853067,
      "fog_index": 300.4855920114123,
      "complex_word_count": 352,
      "word_count": 701,
      "syllables_per_word": 2.9871611982881596,
      "personal_pronouns": 0,
      "avg_word_length": 7.684736091298146,
      "url_id": "Netclan20241159"
    }
  },
  {
    "ID": "Netclan20241160",
    "URL": "https://insights.blackcoffer.com/google-lsa-api-data-automation-and-dashboarding/",
    "Analysis": {
      "positive_score": 33,
      "negative_score": -18,
      "polarity_score": 0.29411758938870797,
      "subjectivity_score": 0.054838709087755816,
      "avg_sentence_length": 930.0,
      "percentage_complex_words": 52.04301075268817,
      "fog_index": 392.81720430107526,
      "complex_word_count": 484,
      "word_count": 930,
      "syllables_per_word": 2.910752688172043,
      "personal_pronouns": 0,
      "avg_word_length": 7.2924731182795695,
      "url_id": "Netclan20241160"
    }
  },
  {
    "ID": "Netclan20241161",
    "URL": "https://insights.blackcoffer.com/healthcare-data-analysis/",
    "Analysis": {
      "positive_score": 24,
      "negative_score": -10,
      "polarity_score": 0.41176458477512207,
      "subjectivity_score": 0.08153477022698394,
      "avg_sentence_length": 417.0,
      "percentage_complex_words": 51.798561151079134,
      "fog_index": 187.51942446043165,
      "complex_word_count": 216,
      "word_count": 417,
      "syllables_per_word": 3.1534772182254196,
      "personal_pronouns": 0,
      "avg_word_length": 7.930455635491607,
      "url_id": "Netclan20241161"
    }
  },
  {
    "ID": "Netclan20241162",
    "URL": "https://insights.blackcoffer.com/budget-sales-kpi-dashboard-using-power-bi/",
    "Analysis": {
      "positive_score": 16,
      "negative_score": -1,
      "polarity_score": 0.882352422145634,
      "subjectivity_score": 0.05029585650012259,
      "avg_sentence_length": 338.0,
      "percentage_complex_words": 50.887573964497044,
      "fog_index": 155.55502958579882,
      "complex_word_count": 172,
      "word_count": 338,
      "syllables_per_word": 3.1923076923076925,
      "personal_pronouns": 0,
      "avg_word_length": 7.994082840236686,
      "url_id": "Netclan20241162"
    }
  },
  {
    "ID": "Netclan20241163",
    "URL": "https://insights.blackcoffer.com/amazon-buy-bot-an-automation-ai-tool-to-auto-checkouts/",
    "Analysis": {
      "positive_score": 17,
      "negative_score": 0,
      "polarity_score": 0.9999994117650519,
      "subjectivity_score": 0.05074626714190248,
      "avg_sentence_length": 335.0,
      "percentage_complex_words": 53.43283582089552,
      "fog_index": 155.37313432835822,
      "complex_word_count": 179,
      "word_count": 335,
      "syllables_per_word": 3.2507462686567163,
      "personal_pronouns": 0,
      "avg_word_length": 8.11044776119403,
      "url_id": "Netclan20241163"
    }
  }
]
with open("output data structure.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "ID", "URL", "positive_score", "negative_score", "polarity_score", 
        "subjectivity_score", "avg_sentence_length", "percentage_complex_words", 
        "fog_index", "complex_word_count", "word_count", "syllables_per_word", 
        "personal_pronouns", "avg_word_length"
    ])

    for record in data:
        try:
            id_ = record["ID"]
            url = record["URL"]

            Analysis = record["Analysis"]

            
            row = [
                id_,
                url,
                Analysis["positive_score"],
                Analysis["negative_score"],
                Analysis["polarity_score"],
                Analysis["subjectivity_score"],
                Analysis["avg_sentence_length"],
                Analysis["percentage_complex_words"],
                Analysis["fog_index"],
                Analysis["complex_word_count"],
                Analysis["word_count"],
                Analysis["syllables_per_word"],
                Analysis["personal_pronouns"],
                Analysis["avg_word_length"]
            ]

       
            writer.writerow(row)

        except Exception as e:
            print(f"Error processing record with ID {record['ID']}: {e}")