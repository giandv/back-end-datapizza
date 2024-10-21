from django.http import JsonResponse
import json
import psycopg2
import os

def index(request):
    json_result = []

    print(os.environ['POSTGRES_USER'])

    #conn = psycopg2.connect(
    #    database="datapizza", user='datapizza_user',
    #    password='pwd', host='postgres', port='5432'
    #)
    #try:
    #    with conn.cursor() as cur:
    #        cur.execute("SELECT job.name,job.schedule," +
    #                    "COALESCE(companies, '[]') AS companies," +
    #                    "COALESCE(technologies, '[]') AS technologies," +
    #                    "COALESCE(infos, '[]') AS infos" +
    #                    "FROM job" +
    #                    "LEFT JOIN LATERAL (" +
    #                    "SELECT json_agg(json_build_object('logo', company.logo," +
    #                    "'name', company.name)) AS companies" +
    #                    "FROM company WHERE  company.job_id = job.id" +
    #                    ")company ON true" +
    #                    "LEFT JOIN LATERAL (" +
    #                    "SELECT json_agg(json_build_object('skillname', technology.skillname)) AS technologies" +
    #                    "FROM technology WHERE  technology.job_id = job.id" +
    #                    ")technology ON true" +
    #                    "LEFT JOIN LATERAL (" +
    #                    "SELECT json_agg(json_build_object('infoname', info.infoname)) AS infos" +
    #                    "FROM info WHERE  info.job_id = job.id" +
    #                    ")info ON true" +
    #                    "ORDER  BY job.id;")
    #        print("The number of parts: ", cur.rowcount)
    #        row = cur.fetchone()

    #        while row is not None:
    #            print(row)
    #            row = cur.fetchone()
    #            json_result.append(row)
    #except (Exception, psycopg2.DatabaseError) as error:
    #    print(error)

    return JsonResponse(json_result, safe=False)

    #     json_result = [
    #   {
    #     "id": 190,
    #     "technologies": [
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 148,
    #         "uuid": "802a0fae-cfbc-47d8-8160-77f356afeea9",
    #         "skillname": "Terraform",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       }
    #     ],
    #     "company": {
    #       "name": "Generali Real Estate",
    #       "tag": "gre",
    #       "logo": "https://api.datapizza.tech/media/companies/4a454315-de4e-4d73-8a96-a7b96c863bfd/generali_real_estate_logo.jpeg"
    #     },
    #     "infos": [
    #       {
    #         "id": 28,
    #         "infoname": "👨🏽‍💻 3-5 Years Experience",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 110,
    #         "infoname": "💸 RAL: 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 281,
    #         "infoname": "📍 Milano Citylife Tretorri",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 288,
    #         "infoname": "💻 3 giorni a settimana in smart",
    #         "color": "green",
    #         "category": "Contract"
    #       }
    #     ],
    #     "name": "Data Engineer",
    #     "emoji": "💻",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 0,
    #     "min_ral_extra": 0,
    #     "max_ral": 0,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 0,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Generali Real Estate sta cercando un Data Engineer da aggiungere al loro team di Data/ML Analytics e Engineering!\r\n\r\n✨ Le tue responsabilità:\r\n\r\n👉 Progettare, sviluppare e monitorare processi ETL\r\n👉 Mettere in produzione e rendere scalabili vari modelli, in ambito GenAI e Computer Vision.\r\n👉 Collaborare con data scientist, analisti e altri stakeholder per comprendere le esigenze di dati e tradurle in soluzioni tecniche\r\n\r\n🔍 Devi applicare solo se:\r\n\r\n👉 Hai una laurea triennale STEM\r\n👉 Hai almeno 3 anni di esperienza nell'ambito Data Engineering\r\n👉 Conosci SQL, AWS e Python\r\n\r\n🏢 La posizione è in sede a Milano Citylife Tre Torri",
    #     "questions": [
    #       "Conosci AWS, SQL e Python?",
    #       "Hai una laurea STEM?",
    #       "Sei disponibile al trasferimento su Milano?"
    #     ],
    #     "open_questions": [],
    #     "uuid": "c70ff67b-5715-439b-85c6-40b6b8b6785a",
    #     "hr_email": [],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "recpSmn0vHxDK2GBr",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-25T12:13:33+02:00",
    #     "updated_at": "2024-10-13T17:53:52.802681+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       37,
    #       48,
    #       68,
    #       148
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 229,
    #     "technologies": [
    #       {
    #         "id": 38,
    #         "uuid": "09576850-c2c3-4a77-979b-0a495af75784",
    #         "skillname": "MySQL",
    #         "color": "warning",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 42,
    #         "uuid": "5799e6b2-e2be-46c9-b200-a42ef9acf452",
    #         "skillname": "MongoDB",
    #         "color": "failure",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 103,
    #         "uuid": "5b2b1066-8164-4100-bf51-cd19095342d0",
    #         "skillname": "Git",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 231,
    #         "uuid": "bad828d3-1006-4da1-ba02-623c8c149c5f",
    #         "skillname": "C# o .Net",
    #         "color": "blue",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Assist Digital",
    #       "tag": "assist_digital",
    #       "logo": "https://api.datapizza.tech/media/companies/4e069e5a-3bbb-4f37-b221-2d9a6a416294/Assist-Digital_logo.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 189,
    #         "infoname": "💳 Bonus & Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 205,
    #         "infoname": "💼 Esperienza 2- 4 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 221,
    #         "infoname": "🏡 Hybrid Roma/ Napoli/ Lecce",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 301,
    #         "infoname": "4gg/mese in sede",
    #         "color": "indigo",
    #         "category": "Other"
    #       }
    #     ],
    #     "name": "Backend Developer",
    #     "emoji": "💻",
    #     "contract": "permanent",
    #     "contract_extra": "",
    #     "schedule": "",
    #     "location": "Roma/ Napoli/ Lecce",
    #     "min_ral": 35000,
    #     "min_ral_extra": 0,
    #     "max_ral": 45000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 2,
    #     "max_work_experience": 4,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Assist Digital è una realtà internazionale che fornisce servizi end-to-end di Customer Experience, combinando intelligenza umana e artificiale.\r\n\r\nTi occuperai di: \r\n👉 Collaborare con il team per la progettazione e lo sviluppo di soluzioni Backend\r\n👉 Definire l'architettura e ottimizzare il software\r\n\r\nSei la persona giusta se:\r\n✅ Hai esperienza con C# o .Net \r\n✅ Conosci bene GIT\r\n✅ Conosci database relazionali e non relazionali (MySQL e MongoDB)\r\n\r\n🚀 Si offrono:\r\n- Buoni Pasto \r\n- Piano di crescita personalizzato\r\n- Welfare e assistenza sanitaria\r\n\r\n🚶🏽‍♀️‍➡️ Step di selezione: Conoscitivo HR + Tecnico",
    #     "questions": [
    #       "Sei disposto ad andare un po' più spesso in una delle sedi per l'onboarding e poi 4gg/mese?",
    #       "Hai esperienza di almeno 2 anni con C# o .Net?"
    #     ],
    #     "open_questions": [
    #       "Come mai pensi di essere la persona giusta per Assist?",
    #       "A quale delle tre location ( Roma/ Napoli/ Lecce) sei interessato/a?",
    #       "Con quale delle tecnologie elencate nell'annuncio ti senti ferrato/a?"
    #     ],
    #     "uuid": "edf922a3-3db8-4576-8903-3d9198d3e7ec",
    #     "hr_email": [
    #       "valentina.ciliesa@assistdigital.com"
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recvsant3uHKyf0aW",
    #     "extra": {
    #       "role": "Backend Developer",
    #       "benefits": "Hybrid Smart Working, A growth path aimed at improving your professionalism, Ticket Restaurant and Corporate welfare, Flexible working hours, Access to our corporate conventions, Internal and external training programs with the possibility to achieve professional certifications according to the role (UXPM1-2-3, Scrum Master, …)",
    #       "requisiti": "You have a degree in technical/scientific disciplines and have gained 3/5 years of experience in the role of ICT services companies where you participated in significant development projects, relating to one or more digital channels (web, mobile...) and in various industries: Telco, Banking, Travel, Utility. 3+ years of full-time development experience. Excellent knowledge of the microservices and event-driven architecture. Fluent in C# and .NET Core. Knowledge of SQL Server. Knowledge of Java and Spring Boot. Knowledge of RabbitMQ, Kafka. Knowledge of containerized environments (Docker, Kubernetes). Knowledge of Code Repository and versioning system (preferably GitLab). Good knowledge of Agile methodologies and tools. Fluency in English (both verbal and written). Team player with strong communication skills. Nice to have: Knowledge of AWS or at least one other cloud provider (i.e. Azure, Google Cloud). Knowledge of Knative, Knowledge of DAPR, Knowledge of MinIO, Knowledge of Istio, Knowledge of Keycloak.",
    #       "work_model": "hybrid",
    #       "day_on_site": "4 Giorni/Mese",
    #       "extra_skills": "",
    #       "schedule_type": "Full-Time",
    #       "extracted_text": "Assist Digital is an international company providing end-to-end customer experience services to global brands. For more than 20 years we have been combining human and artificial intelligence to turn every contact into a valuable opportunity. We are looking for a Backend Developer to join our team. As part of the Assist Digital Digital Factory you will have the opportunity to work on multiple projects, together with experienced Technical Architect, AI/Backend/Frontend Engineers, Product Owners and other stakeholders, to contribute to deliver powered projects. Your responsibilities include participating in the design and development of enterprise web solutions, collaborating closely with multi-disciplinary teams, being involved in meetings with customers, supporting the Project Manager in the technical management of the project, analyzing the feasibility of new projects or new functionalities, and proposing, evaluating, and adopting new technologies to maximize development efficiency.",
    #       "additional_info": "",
    #       "selection_process": "Colloquio HR \nColloquio tecnico",
    #       "hiring_expectation": 1,
    #       "second_requirement": ""
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "true",
    #     "created_at": "2024-09-19T11:16:33+02:00",
    #     "updated_at": "2024-09-26T08:43:56.237629+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       38,
    #       42,
    #       103,
    #       231
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 241,
    #     "technologies": [
    #       {
    #         "id": 66,
    #         "uuid": "5434e8e3-90bb-4ff8-8517-8a8adeed6fa7",
    #         "skillname": "HTML",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 67,
    #         "uuid": "f6a1c1c6-334a-4a0e-b90a-4d44c8a7d2ca",
    #         "skillname": "CSS",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 86,
    #         "uuid": "14c398d1-195e-4c1b-9ec7-18b43606d12c",
    #         "skillname": "Figma",
    #         "color": "failure",
    #         "category": "Design"
    #       }
    #     ],
    #     "company": {
    #       "name": "Adorea Srl",
    #       "tag": "adorea",
    #       "logo": "https://api.datapizza.tech/media/companies/d69c71c6-3ad7-4f12-9403-3bcf54cf92db/WhatsApp_Image_2024-02-15_at_17.17.54.jpeg"
    #     },
    #     "infos": [
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 134,
    #         "infoname": "⏰ Part TIme - 20h/settimana",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 170,
    #         "infoname": "💸 RAL 25k - 28k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 247,
    #         "infoname": "💼 Esperienza: 4 - 6 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Senior UX/UI Designer (Part Time 50%)",
    #     "emoji": "🎨",
    #     "contract": "permanent",
    #     "contract_extra": "",
    #     "schedule": "part_time",
    #     "location": "Full remote",
    #     "min_ral": 25000,
    #     "min_ral_extra": 0,
    #     "max_ral": 28000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 4,
    #     "max_work_experience": 6,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Adorea è una startup automotive che ha deciso di rivoluzionare il mercato B2B lanciando Fleequid.com, il primo marketplace online per la compravendita di veicoli industriali tramite aste.\r\n\r\nÈ alla ricerca di un/una Senior UX/UI Designer Part Time che progetti l’interfaccia del marketplace, rendendo la piattaforma semplice da usare, bella da vedere e irresistibile per gli utenti.\r\n\r\n👉🏼 Sarai owner della UX/UI della piattaforma e collaborerai a stretto contatto con il team Dev\r\n\r\nSei la persona giusta se:\r\n✅ Hai almeno 4 anni di esperienza in sviluppo di interfacce UX/UI per il web\r\n✅ Sei ai tuo agio nel creare wireframe, artwork, prototipi, design system\r\n✅ Sai dialogare con i Dev e non ti spaventi di fronte a HTML e CSS\r\n✅ Figma per te non ha segreti \r\n\r\n🚀 Come Part Time (20 ore la settimana) e in full remote, potrai gestire il tuo tempo con la massima flessibilità\r\n\r\n📍 Selezione: colloquio iniziale, test pratico, valutazione finale",
    #     "questions": [
    #       "Hai almeno 4 anni di esperienza come UX/UI Designer in ambito web?",
    #       "Hai conoscenza avanzata di Figma?",
    #       "È una posizione part time da 20 ore la settimana, con contratto di assunzione. È ok per te?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha portato a candidarti per questa posizione?",
    #       "Racconta brevemente il tuo portfolio e indica un link dove poterlo visionare o, in alternativa, indica link e riferimenti a tuoi lavori passati",
    #       "Hai mai lavorato in Agile insieme a un team di sviluppatori? Racconta la tua esperienza ",
    #       "Che RAL richiedi?"
    #     ],
    #     "uuid": "ae87b589-b97e-46d3-a57b-2dcf9149b196",
    #     "hr_email": [
    #       "claudio.guglielmi@fleequid.com"
    #     ],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recpcPZ7VbLuERzHO",
    #     "extra": {
    #       "role": "Senior UX/UI Designer",
    #       "benefits": "Part-time work with maximum flexibility, full remote work, professional growth opportunities, and supplementary health insurance.",
    #       "requisiti": "Experience with Figma, ability to communicate with developers, understanding of HTML/CSS, and experience in UX/UI design with a portfolio.",
    #       "work_model": "remote",
    #       "day_on_site": "0 Giorni/Mese",
    #       "extra_skills": "",
    #       "schedule_type": "Part-Time",
    #       "extracted_text": "We are a startup launching the first online marketplace for industrial vehicle trading through auctions. You'll develop the interface of our marketplace, owning the UX/UI design. We value autonomy and collaboration with users. The role is part-time, with a focus on flexibility and remote work.",
    #       "additional_info": "",
    #       "responsabilities": "",
    #       "first_requirement": "",
    #       "selection_process": "colloquio iniziale\ntest pratico\nvalutazione finale",
    #       "hiring_expectation": 1,
    #       "second_requirement": ""
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-07T11:35:08+02:00",
    #     "updated_at": "2024-10-17T11:20:02.770427+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       66,
    #       67,
    #       86
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 238,
    #     "technologies": [
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 113,
    #         "uuid": "63b4f89b-4e6c-4e4f-adf3-3a52c9b13c94",
    #         "skillname": "Node.js",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 163,
    #         "uuid": "08081984-cbb6-4ba5-9298-875100052c40",
    #         "skillname": "DevOps",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 173,
    #         "uuid": "983b596c-bebc-4eda-a973-8ee8ca79db3a",
    #         "skillname": "AI",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 174,
    #         "uuid": "0568cd7d-04fd-43da-9eae-f4f9574e540b",
    #         "skillname": "Cloud",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       }
    #     ],
    #     "company": {
    #       "name": "Epiphany",
    #       "tag": "epiphany",
    #       "logo": "https://api.datapizza.tech/media/companies/429deb0d-841c-4d1c-8d9f-bf0e33525ec2/Image.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 71,
    #         "infoname": "👨🏽‍💻 4-7 Years Experience",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 105,
    #         "infoname": "🌟 Equity",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 268,
    #         "infoname": "🔊 Inglese: C1",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 312,
    #         "infoname": "🇪🇺 Full Remote (Europe)",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 314,
    #         "infoname": "💸 Salary: €70k-€100k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Engineering Lead",
    #     "emoji": "🛠️",
    #     "contract": "permanent",
    #     "contract_extra": "p_iva",
    #     "schedule": "full_time",
    #     "location": "Full remote",
    #     "min_ral": 70000,
    #     "min_ral_extra": 0,
    #     "max_ral": 100000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 4,
    #     "max_work_experience": 6,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Epiphany is a Copenhagen based startup, founded by two thought leaders in AI and pedagogy, with a mission to revolutionize how people learn through the science of learning and generative AI and serves clients such as the United Nations, Airbnb, and other Fortune 500 companies.\r\n\r\nIt's looking for an Engineering Lead helping to expand and scale its product and support its growing customer base.\r\n\r\nYou'll:\r\n🌟 Lead the technical development and actively contribute writing code, primarily focusing on back-end enhancements and enterprise security\r\n🌟 Collaborate closely with the co-founders to align technical strategy with business goal\r\n🌟 Ensure the reliability, performance, and security of applications\r\n\r\nYou're the best fit if you have:\r\n✅ Proven experience in a senior technical leadership role\r\n✅ Strong proficiency in Python \r\n✅ Extensive knowledge with DevOps tools and best practices\r\n✅ Experience with Cloud providers, especially AWS \r\n\r\n🆙 Having knowledge with React, Node.js, Generative AI are big pluses\r\n\r\n👉 This is 100% European remote position, C1+ level English is mandatory",
    #     "questions": [
    #       "Do you have at least 4 years of working experience as software engineer?",
    #       "Do you have working experience in DevOps tools and practices?",
    #       "You fluently write and speak English (C1 equivalent level)?"
    #     ],
    #     "open_questions": [
    #       "This is a very operational position, actually without an internal tech team, so you have to code and manage the infrastructure. Especially if you're used to work in a more structured environment, how this it sounds to you? ",
    #       "Tell how many years of professional experience you have with Python and briefly describe the last, significant project you implemented using it",
    #       "Tell about your most significant experience in DevOps field and with a cloud provider (AWS, GCP, Azure) ",
    #       "What is your expected salary?"
    #     ],
    #     "uuid": "4bddbe37-c012-4011-a593-843099cba087",
    #     "hr_email": [
    #       "gianluca@epiphany.education"
    #     ],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "reciH1LBSFCdnbMmF",
    #     "extra": {
    #       "role": "Engineering Lead",
    #       "benefits": "EUR 70k - 110k based on experience + equity to negotiate.",
    #       "requisiti": "Proven experience in a senior technical leadership role, strong proficiency in Python, solid understanding of front-end technologies particularly React, extensive experience with enterprise security practices, and ability to work independently.",
    #       "work_model": "remote",
    #       "day_on_site": "0 Giorni/Mese",
    #       "extra_skills": "",
    #       "schedule_type": "Full-Time",
    #       "extracted_text": "Epiphany is a startup that uses Generative AI and Learning Science to help enterprise companies develop better training programs. The Head of Engineering will lead technical development, focusing on back-end enhancements and enterprise security, and will have the freedom to shape the tech stack. The role involves collaboration with co-founders and mentorship of future team members.",
    #       "additional_info": "",
    #       "responsabilities": "",
    #       "first_requirement": "",
    #       "selection_process": "30 minuti colloquio tecnico e conoscitivo\ncolloquio tecnico\ncolloquio manageriale",
    #       "hiring_expectation": 1,
    #       "second_requirement": ""
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-04T16:17:00+02:00",
    #     "updated_at": "2024-10-18T09:39:36.456846+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       48,
    #       163,
    #       174
    #     ],
    #     "nice_to_have_technologies": [
    #       1,
    #       113,
    #       173
    #     ]
    #   },
    #   {
    #     "id": 217,
    #     "technologies": [
    #       {
    #         "id": 134,
    #         "uuid": "0266c694-c3b9-496f-a585-de2193056a17",
    #         "skillname": "Machine & Deep Learning",
    #         "color": "blue",
    #         "category": "AI Libraries"
    #       },
    #       {
    #         "id": 157,
    #         "uuid": "8d9ae41a-a9d6-423e-b077-d32ea15c94e1",
    #         "skillname": "Geospatial Technologies",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 228,
    #         "uuid": "b6785035-c134-4516-b45a-21a710cbd4be",
    #         "skillname": "Remote Sensing",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 229,
    #         "uuid": "0369d196-db36-4da6-8c9d-a23f84a7047d",
    #         "skillname": "Business Development",
    #         "color": "blue",
    #         "category": "Design"
    #       }
    #     ],
    #     "company": {
    #       "name": "MindEarth",
    #       "tag": "mindearth",
    #       "logo": "https://api.datapizza.tech/media/companies/5c7db10c-0f3c-469a-bd8b-22689a9bd3d9/Screenshot_2024-07-23_alle_16.47.37.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 107,
    #         "infoname": "💸 Bonus basati su performance",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 129,
    #         "infoname": "🔊 Inglese: B2",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 212,
    #         "infoname": "📍Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 303,
    #         "infoname": "💼 Esperienza: 10+ anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 304,
    #         "infoname": "💸 RAL: 80k-100k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 305,
    #         "infoname": "📍Biel (Berna, Svizzera)",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 308,
    #         "infoname": "🌎 Remote working",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Business Developer",
    #     "emoji": "📈",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 80000,
    #     "min_ral_extra": 0,
    #     "max_ral": 100000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 10,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "MindEarth, società che progetta e sviluppa soluzioni basate su localizzazione e dati geospaziali, è alla ricerca di un/una Business Developer a diretto riporto del CEO\r\n\r\nLe tue principali responsabilità saranno:\r\n✨ Sviluppare nuovi prodotti basati sulle soluzioni verticali esistenti\r\n✨ Identificare e sviluppare nuovi mercati in cui adottare e valorizzare l'expertise di MindEarth\r\n✨ Supportare la Direzione nelle attività di product e business development\r\n✨ Mantenere le relazioni con clienti e partner nazionali ed internazionali, adattando le soluzioni a loro specifiche esigenze \r\n\r\nSei la persona ideale se:\r\n✅ Hai consolidata e dimostrabile esperienza nello sviluppo di prodotti e nuove opportunità di business \r\n✅ Hai conoscenze specifiche di remote sensing, geo-computazione e applicazione di machine learning a dati geo spaziali\r\n✅ Provieni da almeno uno di questi settori: Engineering, Energy, Geo-marketing, Beni di consumo, Mobilità \r\n✅ Parli e scrivi fluentemente inglese\r\n\r\n👉 Background tecnico è un big plus\r\n\r\n🆙 Bonus basati su obiettivi",
    #     "questions": [
    #       "Hai esperienza nella gestione di strategie di vendita e nell'identificazione di nuovi clienti in mercati nazionali e internazionali?",
    #       "Hai esperienza con dati relativi a comportamenti dei consumatori, intelligenza di localizzazione, prodotti derivati da immagini satellitari o dati di mobilità?",
    #       "Hai una buona padronanza dell'inglese scritto e parlato?"
    #     ],
    #     "open_questions": [
    #       "Descrivi, citando anche anno e strumenti/tecnologie impiegate, la tua esperienza più significativa utilizzando dati su comportamenti dei consumatori, intelligenza di localizzazione, dati geo spatial o di mobilità",
    #       "Descrivi un'occasione in cui hai identificato e sviluppato una nuova opportunità di business in un nuovo mercato. Quali sfide hai incontrato e come le hai superate?",
    #       "Sei stato scelto/a per il ruolo. Quali sono le azioni che fai nelle prime settimane di lavoro?",
    #       "Qual è la tua richiesta in termini di RAL?"
    #     ],
    #     "uuid": "bbd58067-5a05-4dd0-9b5c-5f760bc50630",
    #     "hr_email": [],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recbXj5idw4Jz10ft",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-09-03T10:47:23+02:00",
    #     "updated_at": "2024-10-10T10:32:46.777015+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       134,
    #       157,
    #       228,
    #       229
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 232,
    #     "technologies": [
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 82,
    #         "uuid": "0d8fe1ea-2f78-4840-9ee1-f4bf685f000b",
    #         "skillname": "Docker",
    #         "color": "success",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 83,
    #         "uuid": "de7ba1f2-642b-4d92-81c6-c3e136969ad5",
    #         "skillname": "Kubernetes",
    #         "color": "gray",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 137,
    #         "uuid": "be9fda1a-d765-48e9-a667-856fb79ef77f",
    #         "skillname": "Database",
    #         "color": "blue",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 163,
    #         "uuid": "08081984-cbb6-4ba5-9298-875100052c40",
    #         "skillname": "DevOps",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 174,
    #         "uuid": "0568cd7d-04fd-43da-9eae-f4f9574e540b",
    #         "skillname": "Cloud",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       }
    #     ],
    #     "company": {
    #       "name": "Datapizza",
    #       "tag": "datapizza",
    #       "logo": "https://api.datapizza.tech/media/companies/4fb78fca-f6fb-487a-8e22-9a0edea6e2ad/channels4_profile.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 96,
    #         "infoname": "🚀 Stock Option Plan",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 168,
    #         "infoname": "👨🏽‍💻 Esperienza: 3+ anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 208,
    #         "infoname": "💸 Buoni pasto €160/mese",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 231,
    #         "infoname": "💸 RAL 40k - 48k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Backend Software Engineer",
    #     "emoji": "🍕",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Full remote",
    #     "min_ral": 40,
    #     "min_ral_extra": 0,
    #     "max_ral": 48,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "In Datapizza, stiamo costruendo un nuovo team di consulenza specializzata nell’integrazione e messa in produzione di soluzioni software per i nostri clienti!\r\n\r\nIl team si occuperà di integrare e gestire l’infrastruttura delle soluzioni sviluppate, garantendo affidabilità, scalabilità e sicurezza.\r\n\r\nIl ruolo richiederà di:\r\n👉🏼 Interagire con i team IT dei clienti per definire le strategie di integrazione nei loro sistemi\r\n👉🏼 Gestire il processo di deployment e messa in produzione in ambienti cloud e on-premise\r\n\r\nFa per te se:\r\n✅ Hai esperienza nell’integrazione e messa in produzione di software in ambienti cloud (AWS, GCP e/o Azure) e on-premise\r\n✅ Conosci e applichi best practice DevOps per garantire affidabilità e scalabilità\r\n✅ Ti piace collaborare con i team dei clienti per trovare soluzioni adatte alle loro esigenze\r\n\r\nStep di selezione: test tecnico + colloquio tecnico e conoscitivo",
    #     "questions": [
    #       "Hai mai messo in produzione in autonomia soluzioni software in cloud e/o on-premise gestendo affidabiità, sicurezza e scalabilità?",
    #       "Sei disponibile a venire sporadicamente in ufficio a Milano per lavorare a stretto contatto con il nostro team AI (qualche giorno ogni 1-2 mesi)?"
    #     ],
    #     "open_questions": [],
    #     "uuid": "33b75f25-24ce-4636-a146-8551d5736afa",
    #     "hr_email": [],
    #     "datapizza_manager_email": "lucaarrotta@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recWKVRY56gWOauBJ",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-01T20:44:34+02:00",
    #     "updated_at": "2024-10-09T10:42:59.442330+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       48,
    #       82,
    #       83,
    #       137,
    #       163,
    #       174
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 215,
    #     "technologies": [
    #       {
    #         "id": 38,
    #         "uuid": "09576850-c2c3-4a77-979b-0a495af75784",
    #         "skillname": "MySQL",
    #         "color": "warning",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 62,
    #         "uuid": "47e98d56-26b9-4bfb-beed-6de72c0b9a08",
    #         "skillname": "PHP",
    #         "color": "indigo",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 11,
    #         "uuid": "170029be-b3b1-4816-b33c-afa381845ec8",
    #         "skillname": "Laravel",
    #         "color": "success",
    #         "category": "Backend"
    #       },
    #       {
    #         "id": 2,
    #         "uuid": "69c482f7-d12c-47ee-bdf2-e0aa5b80204b",
    #         "skillname": "Vue",
    #         "color": "warning",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 82,
    #         "uuid": "0d8fe1ea-2f78-4840-9ee1-f4bf685f000b",
    #         "skillname": "Docker",
    #         "color": "success",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 42,
    #         "uuid": "5799e6b2-e2be-46c9-b200-a42ef9acf452",
    #         "skillname": "MongoDB",
    #         "color": "failure",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "SPIAGGE SRL",
    #       "tag": "spiagge_srl",
    #       "logo": "https://api.datapizza.tech/media/companies/c7b5cc29-9188-4cda-9067-f76f5bfb83b1/logo_spiagge_retro.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 196,
    #         "infoname": "💼 Esperienza: 3-5 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 301,
    #         "infoname": "4gg/mese in sede",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 306,
    #         "infoname": "📍 Rimini",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Backend Developer",
    #     "emoji": "🛠",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Rimini, Province of Rimini, Italy",
    #     "min_ral": 35000,
    #     "min_ral_extra": 0,
    #     "max_ral": 45000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 6,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Spiagge.it è la start-up n.1 in Italia per la prenotazione online di ombrelloni, grazie all'implementazione di un sistema integrato per gestire stabilimenti e prenotazioni sul loro portale \r\n\r\nTi occuperai di:\r\n👉 Sviluppare il core dei sistemi back-end\r\n👉 Creare e migliorare il gestionale, sviluppando nuovi prodotti\r\n\r\nSei la persona giusta se:\r\n✅ Hai esperienza di almeno 3 anni con tecnologie PHP (Laravel) e Vue.js.\r\n✅ Conosci MySQL / MongoDB \r\n✅ Hai esperienza con AWS e Docker\r\n\r\nNice to have:\r\nConoscenza di React e Node\r\n\r\n🎓 Laurea Triennale, preferibilmente ambito STEM\r\n\r\nHybrid Rimini: 4 gg/mese di presenza in ufficio \r\n\r\nSi offrono:\r\n💳 Rimborso spese di viaggio e pernottamento per le giornate in ufficio\r\n\r\nPrevisti 3 colloqui: Colloquio HR + Test Tecnico + Colloquio finale",
    #     "questions": [
    #       "Hai esperienza in entrabe le tecnologie utilizzate PHP (Laravel) e Vue.js.?",
    #       "Hai esperienza con MySQL?",
    #       "Sei disponibile a lavorare 4 giorni al mese consecuitivi su Rimini?"
    #     ],
    #     "open_questions": [
    #       "Come mai hai deciso di candidati per la posizione di Spiagge?"
    #     ],
    #     "uuid": "d7f7f9de-6f05-4e0b-9417-494aa06473d9",
    #     "hr_email": [],
    #     "datapizza_manager_email": "gabriele@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recZTjdo9mtXnZg5P",
    #     "extra": {
    #       "role": "Backend Developer",
    #       "benefits": "Continuous learning opportunities through workshops, courses, and conferences. Work-life balance. Inclusivity and respect for individual uniqueness.",
    #       "requisiti": "4+ years of experience in building digital products. Good knowledge of PHP and Vue.js. Willingness to grow and improve.",
    #       "work_model": "hybrid",
    #       "day_on_site": "4 Giorni/Mese",
    #       "extra_skills": "",
    #       "schedule_type": "Full-Time",
    #       "extracted_text": "Spiagge.it is looking for a Back-end Developer to strengthen the development team. If you love technology and want to make a difference in a collaborative and dynamic environment, keep reading. You will develop and maintain the core of our back-end systems (PHP), create and improve our management system and internal products using Vue.js, and work on our website using Node.js and React.js. We adopt Agile methodologies to remain flexible and responsive. The position is full remote with monthly meetings at our offices in Rimini. You will be at the center of change, responsible for important technical decisions that will define our future and that of our partners. We promote open communication, mutual support, continuous learning, work-life balance, and inclusivity.",
    #       "additional_info": "",
    #       "selection_process": "Colloquio HR\nTest tecnico\nColloquio tecnico con tech lead (solo se si supera il test)\nColloquio CEO",
    #       "hiring_expectation": 1,
    #       "second_requirement": ""
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "true",
    #     "created_at": "2024-08-30T11:12:37+02:00",
    #     "updated_at": "2024-10-16T11:08:35.833021+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       2,
    #       11,
    #       38,
    #       42,
    #       62,
    #       82,
    #       68
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 149,
    #     "technologies": [
    #       {
    #         "id": 67,
    #         "uuid": "f6a1c1c6-334a-4a0e-b90a-4d44c8a7d2ca",
    #         "skillname": "CSS",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 36,
    #         "uuid": "dc5ae2bf-448d-4414-899c-de13cd2f9ec3",
    #         "skillname": "Jira",
    #         "color": "pink",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 66,
    #         "uuid": "5434e8e3-90bb-4ff8-8517-8a8adeed6fa7",
    #         "skillname": "HTML",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 181,
    #         "uuid": "8d45f39e-ea4b-460c-a0d6-fb55be8b85b2",
    #         "skillname": "Frontend",
    #         "color": "blue",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 103,
    #         "uuid": "5b2b1066-8164-4100-bf51-cd19095342d0",
    #         "skillname": "Git",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 54,
    #         "uuid": "5f35e9bd-c430-4c86-b10e-5a56ec0f41ea",
    #         "skillname": "Javascript",
    #         "color": "warning",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 52,
    #         "uuid": "407b1a7f-d675-485b-bb56-c19419f80546",
    #         "skillname": "C#",
    #         "color": "pink",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "C+P Consulting",
    #       "tag": "c+p",
    #       "logo": "https://api.datapizza.tech/media/companies/5413689a-043b-4c4c-8ed1-68102fcf2f7d/Screenshot_2024-07-23_alle_11.01.16.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 129,
    #         "infoname": "🔊 Inglese: B2",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 132,
    #         "infoname": "💼 Esperienza: 3-4 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 275,
    #         "infoname": "📍Bergamo",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Software Engineer",
    #     "emoji": "🔧",
    #     "contract": "permanent",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Bergamo",
    #     "min_ral": 35,
    #     "min_ral_extra": 0,
    #     "max_ral": 40,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "C+P Consulting, innovativa startup tedesca specializzata nel Product Lifecycle Management nel settore Food&Beverage, cerca un/una Software Engineer per la sede italiana \r\n\r\nTi occuperai di:\r\n👉🏼 progettare e implementare nuove funzionalità di applicativi web \r\n👉🏼 integrare servizi di terze parti\r\n👉🏼 supportare tecnicamente business, clienti e fornitori\r\n\r\nFa per te se:\r\n✅ Hai significativa esperienza con C# e ambiente .Net\r\n✅ Utilizzi almeno un framework di FE (es: Angular, React, Vue) \r\n✅ Parli e scrivi correntemente in inglese \r\n✅ Ti interessa crescere sul piano tecnico e organizzativo\r\n\r\n📌 Previsti colloquio conoscitivo e tecnico\r\n\r\n🫡 Potrai fare la differenza, come primo elemento del team tech italiano!\r\n\r\n🆙 Previsti anche bonus!",
    #     "questions": [
    #       "Hai esperienza significativa (almeno 3 anni) con C# come backend e pure di sviluppo Frontend?",
    #       "La posizione prevede anche la presenza fisica nel nuovo ufficio della sede italiana. Sei disposto a lavorare in maniera ibrida, andando in sede 2 gg settimana a Bergamo?",
    #       "Parli e scrivi in inglese correntemente?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per questa posizione?",
    #       "Descrivi un progetto in cui hai usato C# per il backend e un framework di frontend, specificando anche quale",
    #       "Racconta una esperienza in cui hai dovuto lavorare con team esterni o fornitori",
    #       "Qual è la tua richiesta in termini di RAL?"
    #     ],
    #     "uuid": "5b46ab94-6004-44ad-9f4e-574584cfd3c8",
    #     "hr_email": [],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recPH8dXOaVS2XgbT",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-05-24T07:18:33+02:00",
    #     "updated_at": "2024-09-17T16:10:51.645021+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       37,
    #       52,
    #       54,
    #       66,
    #       67,
    #       103,
    #       181
    #     ],
    #     "nice_to_have_technologies": [
    #       36
    #     ]
    #   },
    #   {
    #     "id": 194,
    #     "technologies": [
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 221,
    #         "uuid": "09a8a615-b1ce-425f-a034-1f740c38aa33",
    #         "skillname": "SQLServer",
    #         "color": "blue",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 220,
    #         "uuid": "d021c00b-8023-45eb-90a3-d1faa17e2ae0",
    #         "skillname": "PowerBI o Tableau",
    #         "color": "blue",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 46,
    #         "uuid": "6a9f113b-21a0-493a-9a9d-793e4d677d75",
    #         "skillname": "Oracle",
    #         "color": "indigo",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 100,
    #         "uuid": "ded365d7-71d8-42c9-bd71-0da74ed43343",
    #         "skillname": "Snowflake",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       }
    #     ],
    #     "company": {
    #       "name": "Assist Digital",
    #       "tag": "assist_digital",
    #       "logo": "https://api.datapizza.tech/media/companies/4e069e5a-3bbb-4f37-b221-2d9a6a416294/Assist-Digital_logo.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 60,
    #         "infoname": "💸 RAL 30k-35k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 189,
    #         "infoname": "💳 Bonus & Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 222,
    #         "infoname": "💼 Esperienza 1- 3 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 221,
    #         "infoname": "🏡 Hybrid Roma/ Napoli/ Lecce",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 301,
    #         "infoname": "4gg/mese in sede",
    #         "color": "indigo",
    #         "category": "Other"
    #       }
    #     ],
    #     "name": "Data Engineer",
    #     "emoji": "📈",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Napoli",
    #     "min_ral": 30,
    #     "min_ral_extra": 0,
    #     "max_ral": 35,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 1,
    #     "max_work_experience": 3,
    #     "min_role_experience": 1,
    #     "max_role_experience": 3,
    #     "description": "Assist Digital è una realtà internazionale che fornisce servizi end-to-end di Customer Experience, combinando intelligenza umana e artificiale 🧠\r\n\r\nTi occuperai di: \r\n👉 Analizzare i modelli e gestire il flusso di dati all'interno\r\n👉 Collaborare con il team per disegnare e sviluppare nuove soluzioni di gestione dati\r\n\r\nSei la persona giusta se:\r\n✅ Hai esperienza con Database relazionali e non relazionali\r\n✅ Hai esperienza con PowerBI e/o Tableau \r\n✅ Conosci i principali tool ETL\r\n✅ Hai esperienza con soluzioni per analisi Big Data (es.Spark)\r\n\r\n🚀 Sono garantiti:\r\n- Buoni Pasto \r\n- Piano di crescita personalizzato\r\n- Welfare e assistenza sanitaria\r\n\r\n🚶🏽‍♀️‍➡️ Step di selezione: Conoscitivo, Tecnico e Colloquio Finale",
    #     "questions": [
    #       "Sei disposto a recarti in sede a Napoli 4 volte al mese?",
    #       " Hai esperienza con Database, PowerBI e Oracle?",
    #       "Parli inglese almeno a livello B1/B2?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per Assist Digital?",
    #       " Con quali tecnologie connesse al Data Engineering ti senti particolarmente forte?",
    #       "Hai esperienza con flussi di data integratio, data quality e data management in contesto cloud? Se si, racconta quali tecnologie hai usato e cosa hai gestito"
    #     ],
    #     "uuid": "90d03739-296a-4350-8cf7-302d0dbd3f51",
    #     "hr_email": [],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recgbl2mz0cq64bRG",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-31T09:20:16+02:00",
    #     "updated_at": "2024-09-26T08:43:17.161088+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "Nice to have e non skills obbligatorie (dai 3 anni di exp diventano obbligatorie): esperienza nel disegno e sviluppo di modelli dati, flussi di data integration e data quality, esperienza su soluzioni di data management in contesti cloud (snowflake) o hyperscaler (GCP,AWS), esperienza di programmazione in Python",
    #     "must_have_technologies": [
    #       46,
    #       220,
    #       221
    #     ],
    #     "nice_to_have_technologies": [
    #       48,
    #       68,
    #       100
    #     ]
    #   },
    #   {
    #     "id": 193,
    #     "technologies": [
    #       {
    #         "id": 217,
    #         "uuid": "614becf2-27fe-4e9a-be54-d2e5cfa6d771",
    #         "skillname": "Microsoft 365",
    #         "color": "blue",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 174,
    #         "uuid": "0568cd7d-04fd-43da-9eae-f4f9574e540b",
    #         "skillname": "Cloud",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 218,
    #         "uuid": "2064b4d0-0182-4b3c-89eb-9dbc2738ff09",
    #         "skillname": "LAMP",
    #         "color": "blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 198,
    #         "uuid": "66cbc41e-abeb-4ec0-872b-25dfd35269ce",
    #         "skillname": "Adobe Commerce",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 36,
    #         "uuid": "dc5ae2bf-448d-4414-899c-de13cd2f9ec3",
    #         "skillname": "Jira",
    #         "color": "pink",
    #         "category": "Business Intelligence"
    #       }
    #     ],
    #     "company": {
    #       "name": "50 ml",
    #       "tag": "50ml",
    #       "logo": "https://api.datapizza.tech/media/companies/81b88f2e-1333-4ced-88a3-3def7fe4c8ff/logo_50_ml.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 4,
    #         "infoname": "Corporate Training",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 129,
    #         "infoname": "🔊 Inglese: B2",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 212,
    #         "infoname": "📍Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 228,
    #         "infoname": "💼 Esperienza: 5 - 7 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 234,
    #         "infoname": "💸 RAL 50k - 60k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 291,
    #         "infoname": "🧑🏻‍💻 Anche freelance",
    #         "color": "green",
    #         "category": "Contract"
    #       }
    #     ],
    #     "name": "Tech Lead",
    #     "emoji": "📈",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 50000,
    #     "min_ral_extra": 0,
    #     "max_ral": 60000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 5,
    #     "max_work_experience": 7,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "50 ml, dal 2013 il principale e-commerce italiano di profumi di nicchia, è alla ricerca di un/una Tech Lead che sia il punto di riferimento tecnico dell'Azienda \r\n\r\nTi occuperai di:\r\n👉 Gestire i team di sviluppo remoti\r\n👉 Coordinare progetti per manutenzione ed evoluzione della piattaforma\r\n👉 Fornire supporto tecnico interno\r\n👉 Pianificare la strategia IT dell'Azienda\r\n\r\nSei la persona giusta se:\r\n✅ Hai consolidata esperienza con lo stack LAMP\r\n✅ Hai conoscenza approfondita di customizzazioni di Adobe Commerce Cloud (Magento)\r\n✅ Hai esperienza di gestione progetti IT e team, anche esteri\r\n✅ Hai esperienza sulla integrazione di sistemi di pagamento digitali e POS in ambito retail\r\n\r\nColloquio tecnico/conoscitivo e colloquio finale",
    #     "questions": [
    #       "Hai una esperienza significativa di sviluppo software con Adobe Commerce (Magento)?",
    #       "La posizione prevede anche presenza fisica in sede. Sei disposto/a a lavorare a Milano?",
    #       "Parli e scrivi fluentemente in inglese?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per questa posizione?",
    #       "Descrivi brevemente la tua esperienza di sviluppo con Adobe Commerce",
    #       "Racconta la tua esperienza nella gestione di team",
    #       "Qual è la tua richiesta in termini di RAL?"
    #     ],
    #     "uuid": "4de90fa8-3a08-480d-a173-2c9ad6ca4b09",
    #     "hr_email": [],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recG0gb3Fcv3F1aQA",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-31T08:57:09+02:00",
    #     "updated_at": "2024-09-03T21:46:28.950577+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       36,
    #       174,
    #       198,
    #       217,
    #       218
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 179,
    #     "technologies": [
    #       {
    #         "id": 19,
    #         "uuid": "02091804-4a9a-4afe-ab2f-a06fbe3b2be5",
    #         "skillname": "PyTorch",
    #         "color": "success",
    #         "category": "AI Libraries"
    #       },
    #       {
    #         "id": 210,
    #         "uuid": "d864dff0-bad7-4014-92b3-62e996e54c60",
    #         "skillname": "XGBoost",
    #         "color": "blue",
    #         "category": "AI Libraries"
    #       },
    #       {
    #         "id": 73,
    #         "uuid": "899d33ec-caf0-4cec-b52b-a064da7ce6c7",
    #         "skillname": "Apache Spark",
    #         "color": "warning",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 211,
    #         "uuid": "76c8d235-9304-46d6-97db-73658995f7c7",
    #         "skillname": "GitHub Actions",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "MindEarth",
    #       "tag": "mindearth",
    #       "logo": "https://api.datapizza.tech/media/companies/5c7db10c-0f3c-469a-bd8b-22689a9bd3d9/Screenshot_2024-07-23_alle_16.47.37.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 110,
    #         "infoname": "💸 RAL: 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 129,
    #         "infoname": "🔊 Inglese: B2",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 132,
    #         "infoname": "💼 Esperienza: 3-4 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 212,
    #         "infoname": "📍Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Data Scientist",
    #     "emoji": "🌍",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 40000,
    #     "min_ral_extra": 0,
    #     "max_ral": 50000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 5,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "MindEarth, società che sviluppa soluzioni basate su dati geospaziali, è alla ricerca di un/una Data Scientist\r\n\r\nTi occuperai di:\r\n✨Sviluppare modelli IA su dati satellitari, stradali e di mobilità\r\n✨Processi ETL, Model monitoring e serving, garantendo la corretta implementazione ed erogazione dei modelli \r\n\r\nSei la persona giusta se:\r\n✅ Hai consolidata esperienza nella costruzione di modelli geospaziali e delle tecnologie correlate \r\n✅ Sei in grado di gestire il deployment e l'erogazione dei modelli, adottando pratiche DevOps \r\n✅ Parli fluentemente inglese\r\n\r\n🆙 Conoscenza dello stack per il processamento di big data geospaziali è un grosso plus (geopandas, xarray, Sedona, PostGIS/DuckDB)\r\n\r\n👉 3 colloqui: introduttivo, tecnico, negoziazione",
    #     "questions": [
    #       "Hai esperienza di sviluppo di modelli geospaziali?",
    #       "La posizione prevede anche presenza fisica in sede 2 giorni a settimana. Sei disposto/a a lavorare in centro a Milano?",
    #       "L'inglese è un must. Lo parli e scrivi fluentemente?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per questa posizione?",
    #       "Descrivi brevemente il progetto geospaziale più significativo che hai implementato, con quali tecnologie e in quale anno",
    #       "In quali delle tecnologie elencate ti senti più confidente?",
    #       "Qual è la tua richiesta in termini di RAL?"
    #     ],
    #     "uuid": "a2afe102-c73a-4151-9034-3125d63e36f6",
    #     "hr_email": [],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recGRJyP0vpSDCPe6",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-09T11:47:40+02:00",
    #     "updated_at": "2024-09-30T10:06:39.681319+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       19,
    #       37,
    #       48,
    #       73,
    #       68,
    #       210,
    #       211
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 170,
    #     "technologies": [
    #       {
    #         "id": 113,
    #         "uuid": "63b4f89b-4e6c-4e4f-adf3-3a52c9b13c94",
    #         "skillname": "Node.js",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 67,
    #         "uuid": "f6a1c1c6-334a-4a0e-b90a-4d44c8a7d2ca",
    #         "skillname": "CSS",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 7,
    #         "uuid": "a36ee512-24d3-4178-bcf2-7436878ea843",
    #         "skillname": "Flutter",
    #         "color": "indigo",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 44,
    #         "uuid": "aae638cb-5a5b-4d2c-965f-f0f8d1c606c5",
    #         "skillname": "DynamoDB",
    #         "color": "warning",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 82,
    #         "uuid": "0d8fe1ea-2f78-4840-9ee1-f4bf685f000b",
    #         "skillname": "Docker",
    #         "color": "success",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 66,
    #         "uuid": "5434e8e3-90bb-4ff8-8517-8a8adeed6fa7",
    #         "skillname": "HTML",
    #         "color": "gray",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 103,
    #         "uuid": "5b2b1066-8164-4100-bf51-cd19095342d0",
    #         "skillname": "Git",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 164,
    #         "uuid": "0ed50c3c-e12f-4220-b57b-edf436c6c061",
    #         "skillname": "DB relazionali",
    #         "color": "blue",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "MindEarth",
    #       "tag": "mindearth",
    #       "logo": "https://api.datapizza.tech/media/companies/5c7db10c-0f3c-469a-bd8b-22689a9bd3d9/Screenshot_2024-07-23_alle_16.47.37.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 91,
    #         "infoname": "💸 RAL 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 129,
    #         "infoname": "🔊 Inglese: B2",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 198,
    #         "infoname": "📍 Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 196,
    #         "infoname": "💼 Esperienza: 3-5 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Software Engineer",
    #     "emoji": "🌍",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 40000,
    #     "min_ral_extra": 0,
    #     "max_ral": 50000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 5,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "MindEarth, società nel cuore di Milano che progetta e sviluppa soluzioni basate su localizzazione e dati geospaziali, è alla ricerca di un/una Software Engineer\r\n\r\nTi occuperai di:\r\n✨Sviluppo e manutenzione applicazioni web e mobile, lato FE, BE e dati, relazionali e non \r\n✨Sviluppo e deployment di soluzioni cloud based, garantendone scalabilità e sicurezza\r\n✨Supporto al team Data Science per integrare l'adozione di modelli analitici avanzati\r\n\r\nSei la persona giusta se:\r\n✅ Hai significativa esperienza di sviluppo con React e Node.js\r\n✅ Sei in grado di gestire il deployment e l'erogazione di applicazioni, adottando pratiche DevOps \r\n✅ Parli fluentemente inglese e sei abituato/a ad operare in contesti anche internazionali\r\n\r\n🆙 Esperienza in ambito geospaziale è un mega plus!",
    #     "questions": [
    #       "Hai una esperienza di almeno 3 anni come Software Engineer?",
    #       "La posizione prevede anche presenza fisica in sede 2 giorni la settimana. Sei disposto/a a lavorare in centro a Milano?",
    #       "L'inglese è un must. Lo parli e scrivi fluentemente?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per questa posizione?",
    #       "Descrivi brevemente l'ultimo progetto significativo che hai implementato utilizzando React e Node.js e in quale anno",
    #       "Racconta una tua esperienza in ambito DevOps",
    #       "Qual è la tua richiesta in termini di RAL?"
    #     ],
    #     "uuid": "05307475-7f45-4b58-acdc-483eb43df316",
    #     "hr_email": [],
    #     "datapizza_manager_email": "antonello@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recWIjQfH9sefGTdv",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-06-28T11:46:00+02:00",
    #     "updated_at": "2024-09-30T10:06:55.705445+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       37,
    #       44,
    #       66,
    #       67,
    #       82,
    #       68,
    #       103,
    #       113,
    #       164
    #     ],
    #     "nice_to_have_technologies": [
    #       7
    #     ]
    #   },
    #   {
    #     "id": 178,
    #     "technologies": [
    #       {
    #         "id": 69,
    #         "uuid": "83724127-726f-463a-9121-b0a14d42db6f",
    #         "skillname": "Microsoft Azure",
    #         "color": "warning",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 68,
    #         "uuid": "5081e836-f682-4683-8ad3-c517e0f5f23f",
    #         "skillname": "AWS",
    #         "color": "blue",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 103,
    #         "uuid": "5b2b1066-8164-4100-bf51-cd19095342d0",
    #         "skillname": "Git",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 137,
    #         "uuid": "be9fda1a-d765-48e9-a667-856fb79ef77f",
    #         "skillname": "Database",
    #         "color": "blue",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "Ingegnerie Toscane",
    #       "tag": "Ingegnerie Toscane",
    #       "logo": "https://api.datapizza.tech/media/companies/12e5e076-31d7-4565-a15e-e0f1108b0c1d/ing._toscane_logo.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 60,
    #         "infoname": "💸 RAL 30k-35k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 122,
    #         "infoname": "Benefit: Buoni Pasto da €11",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 202,
    #         "infoname": "💼 Esperienza 1 -2 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 264,
    #         "infoname": "🏡 Hybrid Pisa",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "AI Engineer",
    #     "emoji": "⚙️",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Hybrid Pisa",
    #     "min_ral": 30,
    #     "min_ral_extra": 0,
    #     "max_ral": 35,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 1,
    #     "max_work_experience": 2,
    #     "min_role_experience": 1,
    #     "max_role_experience": 2,
    #     "description": "Ingegnerie Toscane è un'azienda che si occupa di integrare e standardizzare i servizi ingegneristici nel settore idrico-ambientale 💧\r\n\r\nTi occuperai di: \r\n👉 Raccogliere e analizzare i bisogni di miglioramento di tutte le unità aziendali\r\n👉 Essere la figura di riferimento in ambito Ai \r\n👉 Collaborare con un team per l'ottimizzazione dei processi\r\n\r\nSei la persona giusta se: \r\n✅ Hai esperienza con LLM\r\n✅ Conosci GIT, Python e Database (SQL e NoSQL)\r\n✅ Hai esperienza con Azure o AWS\r\n\r\n🎓 Laurea Magistrale, preferibilmente ambito STEM\r\n\r\nHybrid Pisa: 3 gg/settimana di smart working\r\n\r\nSi offrono:\r\n💳 Buoni pasto da 11 Euro\r\n⏱️ Giornata corta ogni venerdì (38.5 ore settimanali) \r\n\r\nPrevisti 2 colloqui: Colloquio HR + colloquio Team Tecnico",
    #     "questions": [
    #       "Hai esperienza nello sviluppo di progetti che integrano modelli di Generative AI, anche a livello personale o accademico?",
    #       "Hai esperienza con LLM e NLP?",
    #       "Sei disposto ad andare a Pisa un paio di volte a settimana?"
    #     ],
    #     "open_questions": [
    #       "Raccontaci di esperimenti e/o progetti che hai realizzato utilizzando modelli di AIGenerativa",
    #       " Potresti descrivere brevemente due idee per progetti basati su modelli di AI Generativa che ritieni possano essere di particolare rilevanza?",
    #       "Considera che devi avviare un progetto che richieda l’uso di modelli di AI Generativa.Quali modelli prenderesti in considerazione tra quelli proprietari (es: GPT) e free-to-use (es: LLAMA)? Su quali criteri baseresti il confronto e la selezione del modello più adatto?"
    #     ],
    #     "uuid": "7d652937-ca5c-447a-9dbf-15a44dad5a4f",
    #     "hr_email": [],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "rec9Xgl9enAjDN44p",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-09T10:22:14+02:00",
    #     "updated_at": "2024-09-13T09:50:49.310519+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       48,
    #       69,
    #       68,
    #       103,
    #       137
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 74,
    #     "technologies": [
    #       {
    #         "id": 28,
    #         "uuid": "81794b7a-9389-475d-9461-cc93f8bd5b82",
    #         "skillname": "PowerBI",
    #         "color": "success",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 182,
    #         "uuid": "4a0b1b1b-15f1-447e-9e63-4f96554f1224",
    #         "skillname": "GenAI",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "ING Bank",
    #       "tag": "ing",
    #       "logo": "https://api.datapizza.tech/media/companies/a9b5389a-96aa-4e49-a920-a753ad2862ca/Progetto_senza_titolo.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 1,
    #         "infoname": "💼 2-3 Years Experience",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 30,
    #         "infoname": "🏠 In sede - Milano",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Software Developer per Sviluppo Chatbot",
    #     "emoji": "🏦",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 0,
    #     "min_ral_extra": 0,
    #     "max_ral": 0,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 0,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "ING sta cercando un appassionato di dati, pronta a contribuire allo sviluppo di un chatbot basato su GenAI e Dialogflow CX.\r\n\r\n✨ Le tue responsabilità:\r\n\r\n👉 Analisi dati per identificare aree di miglioramento del nostro chatbot\r\n👉 Guidare la creazione di dataset di alta qualità e analizzare e interpretare tendenze e modelli\r\n👉 Lavorare con il product owner per prioritizzare esigenze aziendali e implementarle in un approccio analitico.\r\n\r\n🔍 Devi applicare solo se:\r\n\r\n👉 Conosci fluentemente l'inglese\r\n👉 Hai una laurea in Matematica, Economia, Informatica, Ingegneria Gestionale, Statistica.\r\n\r\n❌ La conoscenza di Dialogflow CX è necessaria per ottenere un colloquio",
    #     "questions": {
    #       "questions": [
    #         {
    #           "question": "Conosci e hai esperienza nell'utilizzo di Dialogflow CX?"
    #         },
    #         {
    #           "question": "Vivi o sei disposto a trasferirti a Milano?"
    #         },
    #         {
    #           "question": "Hai un buon livello d'inglese?"
    #         }
    #       ]
    #     },
    #     "open_questions": [
    #       "Hai mai utilizzato sofware o piattaforme per la creazione di Chatbot conversazionali?"
    #     ],
    #     "uuid": "71d61c62-fe99-4468-86ce-69f5177eaac8",
    #     "hr_email": [
    #       "mauro.bernardi@ing.com",
    #       "",
    #       ""
    #     ],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "recLaIrAREQ2g9JAr",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-02-01T11:47:36+01:00",
    #     "updated_at": "2024-10-11T16:55:42.540378+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       28,
    #       37,
    #       48
    #     ],
    #     "nice_to_have_technologies": [
    #       182
    #     ]
    #   },
    #   {
    #     "id": 258,
    #     "technologies": [
    #       {
    #         "id": 224,
    #         "uuid": "871ba15e-366c-402c-bb36-149e359af50c",
    #         "skillname": "Problem Solving",
    #         "color": "blue",
    #         "category": "Design"
    #       },
    #       {
    #         "id": 232,
    #         "uuid": "cfb21fc1-6342-48a4-8cad-a3227c96ca66",
    #         "skillname": "Comunicazione",
    #         "color": "blue",
    #         "category": "Design"
    #       }
    #     ],
    #     "company": {
    #       "name": "Datapizza",
    #       "tag": "datapizza",
    #       "logo": "https://api.datapizza.tech/media/companies/4fb78fca-f6fb-487a-8e22-9a0edea6e2ad/channels4_profile.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 42,
    #         "infoname": "🏠 Hybrid - Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 164,
    #         "infoname": "💸 Buoni Pasto",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 207,
    #         "infoname": "💸 €800/mese",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 245,
    #         "infoname": "Nessuna esperienza richiesta",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Junior Tech Recruiter (Stage)",
    #     "emoji": "👩‍🏫",
    #     "contract": "internship",
    #     "contract_extra": "internship",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 800,
    #     "min_ral_extra": 800,
    #     "max_ral": 800,
    #     "max_ral_extra": 800,
    #     "min_work_experience": 0,
    #     "max_work_experience": 1,
    #     "min_role_experience": 0,
    #     "max_role_experience": 1,
    #     "description": "In Datapizza siamo alla ricerca di una nuova figura di Recruiter da inserire inizialmente in Stage nel nostro Team! 🍕\r\n\r\nTi occuperai di:\r\n\r\n👉🏼 Supportare i talenti della nostra piattaforma nella ricerca di opportunità lavorative \r\n👉🏼 Collaborare con il team per identificare le esigenze dei clienti\r\n👉🏼 Contribuire con le tue idee alla creazione di strategie di recruiting innovative\r\n\r\nSei la persona ideale se:\r\n\r\n✅ Hai interesse per il Tech e l’AI\r\n✅ Hai ottime capacità comunicative e relazionali\r\n✅ Ti piace il nostro stile dinamico (e i nostri meme 😂)\r\n✅ Sei disponibile a lavorare in sede a Milano (Zona Bicocca) almeno 2 giorni a settimana 🏠\r\n\r\n\r\nMust have: \r\nIntraprendenza e voglia di imparare a individuare e attrarre talenti nel settore tech\r\n\r\nNice to have: Master in Risorse Umane \r\n\r\nFull time\r\n🎯 Stage di 6 mesi con finalità di assunzione\r\n\r\nTi aspettiamo nel Team Datapizza! 🍕",
    #     "questions": [
    #       "Vivi a Milano o sei disposto/a recarti in ufficio?",
    #       "Hai la possibilità di recarti in sede 2 o più volte a settimana per il periodo di onboarding?"
    #     ],
    #     "open_questions": [
    #       "Come mai ti candidati per Datapizza? Pensi di essere la persona giusta? Raccontaci qualcosa su di te e sulla tua scelta di intraprendere una carriera in ambito Tech"
    #     ],
    #     "uuid": "509ed21e-7a24-4aba-9253-680fab0e50d0",
    #     "hr_email": [],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recrcBuNXFA0aY6Og",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-07T17:29:40+02:00",
    #     "updated_at": "2024-10-17T16:35:55.292979+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       224,
    #       232
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 257,
    #     "technologies": [
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Sibill",
    #       "tag": "sibill",
    #       "logo": "https://api.datapizza.tech/media/companies/3dca25db-3ceb-4ce0-a319-7fd2973e9c91/Logo_Sibill-FiC-removebg-preview_TaejtnN.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 45,
    #         "infoname": "💸 RAL 50k-70k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 189,
    #         "infoname": "💳 Bonus & Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 247,
    #         "infoname": "💼 Esperienza: 4 - 6 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Middle Frontend Developer",
    #     "emoji": "🧑‍🏫",
    #     "contract": "permanent",
    #     "contract_extra": "permanent",
    #     "schedule": "full_time",
    #     "location": "Full Remote",
    #     "min_ral": 50,
    #     "min_ral_extra": 50,
    #     "max_ral": 70,
    #     "max_ral_extra": 68,
    #     "min_work_experience": 4,
    #     "max_work_experience": 6,
    #     "min_role_experience": 4,
    #     "max_role_experience": 6,
    #     "description": "Sibill è una start-up fintech che sta rivoluzionando la gestione finanziaria delle PMI 💵\r\n\r\nTi occuperai di: \r\n👉 Collaborare con il team per progettare la piattaforma e definirne l'architettura\r\n👉 Creare interfacce utente intuitive \r\n👉 Contribuire al miglioramento del Frontend aggiungendo funzionalità \r\n\r\nSei la persona giusta se: \r\n✅ Hai esperienza con React e TypeScript\r\n\r\nNice to have: \r\n- Conoscenza di Python e Elixir\r\n- Esperienza in aziende di prodotto\r\n\r\n🏡 Full Remote \r\n\r\nSi offrono\r\n💰 Stock option \r\n💳 Buoni pasto \r\n🩺 Assicurazione sanitaria \r\n\r\n3 colloqui previsti: Conoscitivo, Tecnico e Finale con il CEO + offerta",
    #     "questions": [
    #       "Conosci bene React e TypeScript?",
    #       "Hai circa 4 anni di esperienza nel ruolo?"
    #     ],
    #     "open_questions": [
    #       "Racconta brevemente la tua esperienza come Middle Frontend Developer",
    #       " Come mai hai deciso di candidati per Sibill? Quali affinità vedi con il ruolo?"
    #     ],
    #     "uuid": "5a482fe3-87c4-4e3a-be4a-a7fdb36cc9b0",
    #     "hr_email": [
    #       "luca@sibill.it"
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recfzipItf6fW4bSI",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-07T16:14:13+02:00",
    #     "updated_at": "2024-10-09T14:28:12.555660+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       6
    #     ],
    #     "nice_to_have_technologies": [
    #       48
    #     ]
    #   },
    #   {
    #     "id": 256,
    #     "technologies": [
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Sibill",
    #       "tag": "sibill",
    #       "logo": "https://api.datapizza.tech/media/companies/3dca25db-3ceb-4ce0-a319-7fd2973e9c91/Logo_Sibill-FiC-removebg-preview_TaejtnN.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 189,
    #         "infoname": "💳 Bonus & Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 223,
    #         "infoname": "💼 Esperienza: 7-10 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 289,
    #         "infoname": "💸 RAL 70k-90k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Senior Frontend Developer",
    #     "emoji": "🧑‍💻",
    #     "contract": "permanent",
    #     "contract_extra": "permanent",
    #     "schedule": "full_time",
    #     "location": "Full Remote",
    #     "min_ral": 70,
    #     "min_ral_extra": 70,
    #     "max_ral": 90,
    #     "max_ral_extra": 90,
    #     "min_work_experience": 7,
    #     "max_work_experience": 10,
    #     "min_role_experience": 7,
    #     "max_role_experience": 10,
    #     "description": "Sibill è una start-up fintech che sta rivoluzionando la gestione finanziaria delle PMI 💵\r\n\r\nTi occuperai di: \r\n👉 Collaborare con il CTO per progettare la piattaforma e definirne l'architettura\r\n👉 Creare interfacce utente intuitive \r\n👉 Contribuire al miglioramento del Frontend aggiungendo funzionalità \r\n\r\nSei la persona giusta se: \r\n✅ Hai esperienza con React e TypeScript\r\n\r\nNice to have: \r\n- Conoscenza di Python e Elixir\r\n- Esperienza in aziende di prodotto\r\n\r\n🏡 Full Remote \r\n\r\nSi offrono\r\n💰 Stock option \r\n💳 Buoni pasto \r\n🩺 Assicurazione sanitaria \r\n\r\n3 colloqui previsti: Conoscitivo, Tecnico e Finale con il CEO + offerta",
    #     "questions": [
    #       "Conosci bene React e TypeScript?",
    #       "Hai circa 7 anni di esperienza nel ruolo?"
    #     ],
    #     "open_questions": [
    #       "Racconta brevemente la tua esperienza come Senior Frontend Developer",
    #       " Come mai hai deciso di candidati per Sibill? Quali affinità vedi con il ruolo?"
    #     ],
    #     "uuid": "e2867a23-0f50-47c0-9861-3338252197d0",
    #     "hr_email": [
    #       "luca@sibill.it"
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recYhf8HvFvY5RwDw",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-07T15:58:49+02:00",
    #     "updated_at": "2024-10-18T11:51:05.355146+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       6
    #     ],
    #     "nice_to_have_technologies": [
    #       48
    #     ]
    #   },
    #   {
    #     "id": 252,
    #     "technologies": [
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 180,
    #         "uuid": "c0cb7428-d7ae-492b-9fa2-e80374b43799",
    #         "skillname": "Elixir",
    #         "color": "blue",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Sibill",
    #       "tag": "sibill",
    #       "logo": "https://api.datapizza.tech/media/companies/3dca25db-3ceb-4ce0-a319-7fd2973e9c91/Logo_Sibill-FiC-removebg-preview_TaejtnN.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 45,
    #         "infoname": "💸 RAL 50k-70k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 189,
    #         "infoname": "💳 Bonus & Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 247,
    #         "infoname": "💼 Esperienza: 4 - 6 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Middle Backend Developer",
    #     "emoji": "😎",
    #     "contract": "permanent",
    #     "contract_extra": "permanent",
    #     "schedule": "full_time",
    #     "location": "Full Remote",
    #     "min_ral": 50,
    #     "min_ral_extra": 0,
    #     "max_ral": 70,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 4,
    #     "max_work_experience": 6,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Sibill è una start-up fintech che sta rivoluzionando la gestione finanziaria delle PMI 💵\r\n\r\nTi occuperai di: \r\n 👉 Collaborare con il team per progettare la piattaforma e definirne l'architettura\r\n👉 Gestire le integrazioni e lo sviluppo di API per la sincronizzazione dei dati\r\n👉 Contribuire al miglioramento del Backend aggiungendo funzionalità \r\n\r\nSei la persona giusta se: \r\n✅ Hai esperienza con linguaggi di programmazione funzionali\r\n\r\nNice to have: \r\n- Programmazione in Elixir\r\n- Conoscenza di Python e TypeScript\r\n- Esperienza in aziende di prodotto\r\n\r\n🏡 Full Remote \r\n\r\nSi offrono\r\n💰 Stock option \r\n💳 Buoni pasto \r\n🩺 Assicurazione sanitaria \r\n\r\n3 colloqui previsti: Conoscitivo, Tecnico e Finale con il CEO + offerta",
    #     "questions": [
    #       "Conosci Elixir o altri linguaggi di programmazione funzionali?",
    #       "Hai circa 4 anni di esperienza nel ruolo?"
    #     ],
    #     "open_questions": [
    #       "Racconta brevemente la tua esperienza come Backend Developer e quali tipi di tecnologie hai usato lato programmazione funzionale",
    #       " Come mai hai deciso di candidati per Sibill? Quali affinità vedi con il ruolo?"
    #     ],
    #     "uuid": "20cedf62-2021-4e27-bc63-a9ec2cfb6998",
    #     "hr_email": [
    #       "luca@sibill.it"
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recAtLihRVrsN7DEQ",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-07T15:32:56+02:00",
    #     "updated_at": "2024-10-14T17:24:27.278651+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       6,
    #       180
    #     ],
    #     "nice_to_have_technologies": [
    #       48
    #     ]
    #   },
    #   {
    #     "id": 197,
    #     "technologies": [
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "Reale Group",
    #       "tag": "reale_group",
    #       "logo": "https://api.datapizza.tech/media/companies/ce31f923-1964-4fa8-ad05-2d69b7021c43/Reale-Group-HiRes-Rettangolare.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 35,
    #         "infoname": "🔋 Corporate Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 166,
    #         "infoname": "👨‍💻 2+ anni esperienza",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 296,
    #         "infoname": "🎓 Laurea ambito STEM o Economia",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 297,
    #         "infoname": "🏡 Torino/ Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 294,
    #         "infoname": "12gg/ mese di smart",
    #         "color": "green",
    #         "category": "Contract"
    #       }
    #     ],
    #     "name": "Analista Funzionale",
    #     "emoji": "💻",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Torino / Milano",
    #     "min_ral": 35,
    #     "min_ral_extra": 0,
    #     "max_ral": 45,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 2,
    #     "max_work_experience": 7,
    #     "min_role_experience": 2,
    #     "max_role_experience": 5,
    #     "description": "Reale Group,una delle più grandi compagnie assicurative d'Italia, ha intrapreso un percorso di rinnovo in ambito tecnologico per rendere i suoi processi sempre più efficienti e all'avanguardia. \r\n\r\nTi occuperai di: \r\n👉 Collaborare con il business per raccogliere i requisiti tecnici\r\n👉 Tradurre le necessità del business agli sviluppatori IT\r\n👉 Fare testing delle soluzioni\r\n\r\nSei la persona giusta se: \r\n✅ Hai esperienza di almeno 2 anni con SQL\r\n✅ Hai conoscenze dei principi di Contabilità e Bilancio \r\n\r\nNice to have: \r\nConoscenza di Java e JavaScript\r\nConoscenza di PASS Portal \r\n\r\n🎓 Laurea in ambito STEM o Economia\r\n\r\n📍Torino/ Milano - con 12gg/ mese di smart da gestire come vuoi + settimana da 37 ore\r\n\r\nSi offrono: \r\nAgevolazioni per dipendenti e buoni pasto (7€ Torino e 9.50€ Milano)",
    #     "questions": [
    #       "Vivi a Torino/Milano o sei disposto a trasferirti?",
    #       " Ti sei già occupato di IT Analysis?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha spinto a candidarti per questa posizione presso Reale Group?",
    #       "Hai ricoperto un ruolo in cui dovevi fare da tramite per il business verso degli sviluppatori esterni?",
    #       "Hai esperienza con il codice/vieni da esperienze tecniche? Conosci i principi di contabilità e bilancio?Se si, racconta brevemente di cosa ti sei occupato/a e quali similarità hai notato con il ruolo"
    #     ],
    #     "uuid": "49fa61b4-6947-4a73-952d-eb3baab35c72",
    #     "hr_email": [
    #       "tania.brusamolin@realeites.com "
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recoV8u32cwjIdR3D",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-08-01T17:49:17+02:00",
    #     "updated_at": "2024-09-04T09:47:32.998815+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "Hanno sede sia a Torino che a Milano ma adesso sono più concentrati su Torino. \r\nIl profilo deve avere conoscenze tecniche quindi laureato in Informatica, Economia o Ingegneria Gestionale. Il suo ruolo consiste nel fare da tramite tra il business e i consulenti esterni che mettono mano al codice della loro piattaforma. La persona dunque deve: \r\n- Capire le necessità di dominio,\r\n- Interfacciarsi con il business per raccogliere evolutive e problemi vari\r\n- prevenire certi problemi grazie alle sue conoscenze tecniche bloccando il business sul nascere qualora proponessero cose infattibili\r\n- Parlare con i tecnici e trasmettere i bisogni per poi testare il codice \r\n- Deve avere conoscenze in ambito bilancio perchè collaborerà con l'area contabilità\r\n\r\nConoscenze tecniche: SQL ( Must have) \r\nJava e JavaScript ( nice to have) per la questione di capire e testare il codice e parlare con i tecnici sviluppatori esterni\r\n\r\nImportante: La persona NON deve lavorare per aziende che gestiscono progetti di Reale Mutua in consulenza, nè avere parenti che lavorano per Reale Mutua \r\n\r\nStanno creando un dipartimento Agile dove si collocherà poi anche l'IT Analyst che per il momento opera in Waterfall. Questa figura collaborerà con il Porduct Owner e con il Business Analyst per tradurre i requisiti di business. \r\n\r\nSoft Skill: Leadership, comunicazione sia in italiano che in inglese (livello B1 che verrà testato) \r\nresilienza, orientamento al cliente e altre",
    #     "must_have_technologies": [
    #       37
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 186,
    #     "technologies": [
    #       {
    #         "id": 53,
    #         "uuid": "1ae80646-ec34-493d-aa94-5fd84bf20037",
    #         "skillname": "Java",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 116,
    #         "uuid": "712d0dc9-114c-441c-aa2b-f536d419f812",
    #         "skillname": "REST API",
    #         "color": "Blue",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 42,
    #         "uuid": "5799e6b2-e2be-46c9-b200-a42ef9acf452",
    #         "skillname": "MongoDB",
    #         "color": "failure",
    #         "category": "Database"
    #       }
    #     ],
    #     "company": {
    #       "name": "DOS Design",
    #       "tag": "DOS Design",
    #       "logo": "https://api.datapizza.tech/media/companies/7f8eee28-aa72-4d32-a58e-6f2903cf822e/Dos_Design.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 11,
    #         "infoname": "📈 Benefit e Bonus",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 91,
    #         "infoname": "💸 RAL 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 205,
    #         "infoname": "💼 Esperienza 2- 4 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Backend Developer",
    #     "emoji": "🛠",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Remote",
    #     "min_ral": 40,
    #     "min_ral_extra": 0,
    #     "max_ral": 50,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 2,
    #     "max_work_experience": 4,
    #     "min_role_experience": 2,
    #     "max_role_experience": 4,
    #     "description": "DOS promuove l’integrazione di AI Solution capaci di accompagnare il processo di cambiamento delle persone. Lavorerai in un team con mindset orientato al prodotto, in squad multidisciplinari dove la cura del Team viene prima di tutto.\r\n\r\n\r\nTi occuperai di:\r\n👉🏼 Sviluppare e mantenere servizi backend e API RESTful\r\n👉🏼 Lavorare con database relazionali e non relazionali\r\n👉🏼 Creare una super squadra con i colleghi frontend e colleghi di team \r\n\r\nSei la persona giusta se:\r\n✅ Conosci Python\r\n✅ Hai esperienza RESTful APIs (FastAPI, Flask o simili)\r\n✅ Hai confidenza con database relazionali e non relazionali (MongoDB)\r\n\r\nNice to have: \r\n📍 Utilizzi Kubernetes e Docker\r\n📍 Hai esperienza Cloud Platform (AWS, GCP)\r\n📍 Esperienza con Java\r\n\r\n\r\n📅 Esperienza 2-4 anni\r\n🕵️‍♀️ Tre step di colloquio",
    #     "questions": [
    #       "Hai ottimo esperienza sia di Python che RESTful APIS?",
    #       "Hai almeno 2 anni di esperienza nel ruolo?",
    #       "Hai confidenza con i database relazionali e non relazionali?"
    #     ],
    #     "open_questions": [
    #       "Quali sono le skill Nice to Have che conosci?",
    #       "Cosa ti ha convinto a candidarti per questa opportunità?",
    #       "Puoi raccontarci un progetto che hai seguito utilizzando lo stack richiesto?"
    #     ],
    #     "uuid": "3ca8273a-c4b4-4d92-839e-1c70fb3236c3",
    #     "hr_email": [],
    #     "datapizza_manager_email": "isaia.laudi@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recABRoGZefcRyN7r",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-10T14:52:11.758683+02:00",
    #     "updated_at": "2024-09-03T21:46:28.741843+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       37,
    #       42,
    #       48,
    #       53,
    #       116
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 182,
    #     "technologies": [
    #       {
    #         "id": 206,
    #         "uuid": "c0d1c853-1d60-45d1-a115-1f2161daf47c",
    #         "skillname": "Camunda",
    #         "color": "blue",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 53,
    #         "uuid": "1ae80646-ec34-493d-aa94-5fd84bf20037",
    #         "skillname": "Java",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 222,
    #         "uuid": "f090084d-fb8f-4234-b2c6-04fe816557cb",
    #         "skillname": "Drools",
    #         "color": "blue",
    #         "category": "Tech Infrastructure"
    #       }
    #     ],
    #     "company": {
    #       "name": "DOS Design",
    #       "tag": "DOS Design",
    #       "logo": "https://api.datapizza.tech/media/companies/7f8eee28-aa72-4d32-a58e-6f2903cf822e/Dos_Design.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 11,
    #         "infoname": "📈 Benefit e Bonus",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 21,
    #         "infoname": "🏠 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 91,
    #         "infoname": "💸 RAL 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 295,
    #         "infoname": "💼 Esperienza 2 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       }
    #     ],
    #     "name": "Process Engineer",
    #     "emoji": "📈",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Remote",
    #     "min_ral": 40,
    #     "min_ral_extra": 0,
    #     "max_ral": 50,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 2,
    #     "max_work_experience": 2,
    #     "min_role_experience": 2,
    #     "max_role_experience": 2,
    #     "description": "DOS promuove l’integrazione di AI Solution capaci di accompagnare il processo di cambiamento delle persone. Lavorerai in un team con mindset orientato al prodotto, in squad multidisciplinari dove la cura del Team viene prima di tutto.\r\n\r\n\r\nTi occuperai di:\r\n👉🏼 Progettare e implementare processi aziendali utilizzando la notazione BPMN\r\n👉🏼 Definire e gestire le regole aziendali con DMN e DRL\r\n👉🏼 Collaborare con i team di sviluppo per integrare le regole nelle applicazioni\r\n \r\n\r\nSei la persona giusta se:\r\n✅ Hai competenza nella notazione BPMN\r\n✅ Hai esperienza con la notazione DMN\r\n✅ Hai conoscenza di Python e Java\r\n \r\nNice to have: \r\n📍 Drools \r\n📍 Camunda\r\n\r\n\r\n📅 Esperienza 2 anni\r\n🕵️‍♀️ Tre colloqui: conoscitivo, tecnico e di approfondimento",
    #     "questions": [
    #       "Hai almeno 2 anni di esperienza con la notazione BPMN?",
    #       " Hai esperienza con la notazione DMN?",
    #       " Conosci sia Python che Java?"
    #     ],
    #     "open_questions": [
    #       "Cosa ti ha convinto a candidarti per questa opportunità?",
    #       "Puoi raccontarci un progetto che hai seguito utilizzando la notazione BPMN?",
    #       "Quanti anni di esperienza hai con le notazioni richieste?"
    #     ],
    #     "uuid": "9cb16095-f979-4bc9-ad29-6fccb19eeb1c",
    #     "hr_email": [],
    #     "datapizza_manager_email": "isaia.laudi@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recQ3CdKdAp1m0Jv0",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-07-10T10:25:08+02:00",
    #     "updated_at": "2024-09-17T15:22:53.149421+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       53
    #     ],
    #     "nice_to_have_technologies": [
    #       48,
    #       206,
    #       222
    #     ]
    #   },
    #   {
    #     "id": 167,
    #     "technologies": [
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 54,
    #         "uuid": "5f35e9bd-c430-4c86-b10e-5a56ec0f41ea",
    #         "skillname": "Javascript",
    #         "color": "warning",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 205,
    #         "uuid": "e3529435-92a3-4d37-93b3-22fa779e08a6",
    #         "skillname": ".NET",
    #         "color": "blue",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Techimp - Doble Engineering",
    #       "tag": "Techimp - Doble Engineering",
    #       "logo": "https://api.datapizza.tech/media/companies/83d548a3-c6b4-4862-8f18-638aab56b4e9/techimp-doble-nodobleco-sidebyside-v100.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 91,
    #         "infoname": "💸 RAL 40k-50k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 171,
    #         "infoname": "🏠 Ibrido a Bologna",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 230,
    #         "infoname": "💻 Smart 3 giorni/ settimana",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 236,
    #         "infoname": "💼 Esperienza 5 - 6 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 255,
    #         "infoname": "🤑Buoni pasto e assicurazione sanitaria",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Full Stack Developer",
    #     "emoji": "🖥",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Bologna",
    #     "min_ral": 35,
    #     "min_ral_extra": 0,
    #     "max_ral": 50,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 5,
    #     "max_work_experience": 6,
    #     "min_role_experience": 5,
    #     "max_role_experience": 6,
    #     "description": "Il team di Doble Engineering fornisce soluzioni di diagnostica e competenza ingegneristica per garantire energia affidabile e sicura. Da oltre un secolo supporta la gestione e la manutenzione dei sistemi elettrici con un occhio alle tecnologie emergenti.\r\n\r\nTi occuperai di \r\n👉🏼 Analisi dei requisiti\r\n👉🏼 Intero ciclo di sviluppo compresa la fase di testing\r\n\r\nSei la persona giusta se\r\n✅ Sei un mago di .NET\r\n✅ Conosci framework Javascript\r\n✅ Hai solide basi di ingegneria del software\r\n\r\n🏠 3 giorni di smartworking a settimana\r\n🏢 Sede: Bologna\r\n\r\n💵 Assicurazione sanitaria e buoni pasto\r\n\r\n📅 Esperienza 5-6 anni",
    #     "questions": [
    #       "Sei disponibile ad andare 2 giorni a settimana in sede a Bologna?",
    #       "Hai almeno 5 anni di esperienza?",
    #       "Conosci bene .NET e Javascript?"
    #     ],
    #     "open_questions": [
    #       "Puoi raccontarci un esempio di progetto in .NET su cui hai lavorato?",
    #       "Quanta esperienza hai nella gestione dell'ingegneria del software?",
    #       "Cosa ti ha spinto a candidarti per la posizione? Quale aspetto ti interessa di più e vedi affine con la tua esperienza?"
    #     ],
    #     "uuid": "7bfd5f36-bb2d-4bee-b39e-385efea5aab7",
    #     "hr_email": [
    #       "ACaprara@doble.com",
    #       "ADiPede@doble.com",
    #       "SPorrini@doble.com",
    #       "",
    #       "",
    #       ""
    #     ],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "rec2rFssd8jjT1hlE",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-06-26T12:47:56.561482+02:00",
    #     "updated_at": "2024-09-03T21:46:28.963223+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       37,
    #       54,
    #       205
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 129,
    #     "technologies": [
    #       {
    #         "id": 51,
    #         "uuid": "986e511a-0ae4-4e03-a43d-a1e9cc50c379",
    #         "skillname": "C++",
    #         "color": "purple",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 52,
    #         "uuid": "407b1a7f-d675-485b-bb56-c19419f80546",
    #         "skillname": "C#",
    #         "color": "pink",
    #         "category": "Coding"
    #       }
    #     ],
    #     "company": {
    #       "name": "Gilardoni",
    #       "tag": "gilardoni",
    #       "logo": "https://api.datapizza.tech/media/companies/7d194d05-9c9b-4352-b0aa-9f6c893808f3/Bottega_52_-_Grafiche_5.png"
    #     },
    #     "infos": [
    #       {
    #         "id": 35,
    #         "infoname": "🔋 Corporate Benefits",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 83,
    #         "infoname": "🏠 In presenza",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 132,
    #         "infoname": "💼 Esperienza: 3-4 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 201,
    #         "infoname": "💸 RAL 45k - 55k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Software Developer Image Recognition",
    #     "emoji": "🤖",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Lonate Ceppino",
    #     "min_ral": 45,
    #     "min_ral_extra": 0,
    #     "max_ral": 55,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 3,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "Gilardoni è uno dei principali operatori nell’ambito dei controlli non distruttivi a raggi X al mondo. L’applicazione dei loro impianti svaria dai controlli aeroportuali al settore alimentare garantendo qualità e sicurezza.\r\n\r\nSarà tuo compito\r\n👉🏼 Progettare e sviluppare software di image recognition per sistemi a Raggi X\r\n👉🏼 Personalizzare i software in base alle specifiche del singolo progetto\r\n👉🏼 Interfacciarti con il team cross funzionale che si occupa di realizzare gli impianti\r\n\r\nFa per te se\r\n✅ Hai un background informatico\r\n✅ Hai esperienza in ambito automazione con C# e C++\r\n✅ Sei sei appassionato di sviluppo in ambito industriale nello specifico image recognition\r\n\r\n💳 Ticket Restaurant, formazione, smart working in fase di progettazione \r\n\r\n📍In presenza a Lonate Ceppino (VA)\r\n\r\n🔗 2 colloqui: conoscitivo da remoto, tecnico in presenza",
    #     "questions": [
    #       {
    #         "question": "Sei disponibile a lavorare in presenza a Lonate Ceppino (VA)?"
    #       },
    #       {
    #         "question": "Sei interessata/o a lavorare nel settore dell'automazione?"
    #       }
    #     ],
    #     "open_questions": [
    #       "Scrivi qui sotto una breve presentazione di te in termini di educazione, esperienza ed obiettivi di carriera.",
    #       "Cosa ti ha interessato maggiormente nella posizione?",
    #       "Come te la cavi con le tecnologie richieste?"
    #     ],
    #     "uuid": "df136573-56b7-4ee5-9644-196a6f3b079d",
    #     "hr_email": [
    #       "chiara.ciniselli@gilardoni.it"
    #     ],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "rec0NDP935NE3kFWL",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-04-24T11:47:36+02:00",
    #     "updated_at": "2024-10-03T15:22:24.402301+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       51,
    #       52
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 268,
    #     "technologies": [
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 8,
    #         "uuid": "16d066ef-7cd4-46e7-bad1-7083eddb2195",
    #         "skillname": "Django",
    #         "color": "success",
    #         "category": "Backend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 150,
    #         "uuid": "dab5c5cf-9259-4418-91f1-fe9d43e57559",
    #         "skillname": "Next.JS",
    #         "color": "red",
    #         "category": "Frontend"
    #       }
    #     ],
    #     "company": {
    #       "name": "Datapizza",
    #       "tag": "datapizza",
    #       "logo": "https://api.datapizza.tech/media/companies/4fb78fca-f6fb-487a-8e22-9a0edea6e2ad/channels4_profile.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 19,
    #         "infoname": "🧑‍💻 Esperienza: 2-5 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 73,
    #         "infoname": "🌎 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 96,
    #         "infoname": "🚀 Stock Option Plan",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 138,
    #         "infoname": "🏖️ Retreat fighissimi",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 208,
    #         "infoname": "💸 Buoni pasto €160/mese",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 318,
    #         "infoname": "💸 RAL: 32k - 36k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Frontend Developer",
    #     "emoji": "🍕",
    #     "contract": "permanent",
    #     "contract_extra": "permanent",
    #     "schedule": "full_time",
    #     "location": "Full Remote",
    #     "min_ral": 32000,
    #     "min_ral_extra": 0,
    #     "max_ral": 36000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 0,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Vuoi entrare a far parte del Team di Datapizza? 🍕\r\n\r\nSiamo alla ricerca di una nuova aggiunta al nostro team, per ricoprire il ruolo di \r\nTi occuperai di aiutarci nello sviluppo della piattaforma su cui ti stai candidando e di altre cose fighissime.\r\n\r\nMa che caratteristiche ha la figura che stiamo cercando?\r\n\r\n💎 Ha esperienza nello sviluppo Frontend.\r\n🧱 Non ha paura di sporcarsi le mani con il Backend.\r\n🐳 Se parla di container non si riferisce alle spedizioni.\r\n\r\nQuesta opportunità fa per te se:\r\n\r\n🫡 Hai voglia di fare la differenza.\r\n🚀 Vuoi far parte di una startup vivace contribuendo attivamente al progetto Datapizza.\r\n\r\nProcesso di selezione:\r\n✅ Test tecnico (Django + React)\r\n✅ Colloquio tecnico\r\n✅ Colloquio Attitudinale",
    #     "questions": [
    #       "Ti ritieni più improntato al Frontend rispetto che al Backend?",
    #       "Sei aperto a una collaborazione Full Time a lungo termine?",
    #       "Hai maturato almeno un anno e mezzo di esperienza come Frontend developer?"
    #     ],
    #     "open_questions": [
    #       "Perché ti ritieni in grado di sviluppare in React e Django?",
    #       "Hai interesse o praticità in ambito UX/UI ?",
    #       "Dovendo auto valutare le tue skill in Typescript come ti descriveresti?",
    #       "Scrivi qui sotto una breve presentazione di te in termini di educazione, esperienza e obiettivi di carriera"
    #     ],
    #     "uuid": "c6bf5e4c-8d39-4bf7-a394-36045ac2e35d",
    #     "hr_email": [],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recXeNyWEsTiZivte",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-10-17T18:19:37+02:00",
    #     "updated_at": "2024-10-18T11:54:55.237881+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       6,
    #       8,
    #       48
    #     ],
    #     "nice_to_have_technologies": [
    #       150
    #     ]
    #   },
    #   {
    #     "id": 242,
    #     "technologies": [
    #       {
    #         "id": 28,
    #         "uuid": "81794b7a-9389-475d-9461-cc93f8bd5b82",
    #         "skillname": "PowerBI",
    #         "color": "success",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 42,
    #         "uuid": "5799e6b2-e2be-46c9-b200-a42ef9acf452",
    #         "skillname": "MongoDB",
    #         "color": "failure",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 99,
    #         "uuid": "86330ae0-7e6e-46de-8ffb-9b4db2365810",
    #         "skillname": "Qlik",
    #         "color": "blue",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 129,
    #         "uuid": "c92775c9-2c2d-45e5-ba6d-19350cf44506",
    #         "skillname": "Pandas",
    #         "color": "blue",
    #         "category": "AI Libraries"
    #       }
    #     ],
    #     "company": {
    #       "name": "Il Sole 24 ORE",
    #       "tag": "il_sole_24_ore",
    #       "logo": "https://api.datapizza.tech/media/companies/d6e9c6a2-1949-4f47-a86f-cbb56e0142bb/Logo_Sole.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 10,
    #         "infoname": "🧑🏽‍💻 Lavoro Ibrido",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 19,
    #         "infoname": "🧑‍💻 Esperienza: 2-5 anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 198,
    #         "infoname": "📍 Milano",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 199,
    #         "infoname": "💻 Smart 2 giorni/settimana",
    #         "color": "green",
    #         "category": "Contract"
    #       }
    #     ],
    #     "name": "Data Analyst Specialist",
    #     "emoji": "📊",
    #     "contract": "permanent",
    #     "contract_extra": "permanent",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 35000,
    #     "min_ral_extra": 0,
    #     "max_ral": 45000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 2,
    #     "max_work_experience": 5,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "Sole 24 Ore cerca un/una Data Analyst Specialist per l'area Business Data Management.\r\n\r\nTi occuperai di:\r\n👉 Estrarre e analizzare dati da fonti multiple per creare report e insight.\r\n👉 Supportare campagne di marketing con targeting e analisi.\r\n👉 Partecipare a progetti di Data-Driven Strategy e Marketing Automation.\r\n\r\nSei la persona giusta se:\r\n✅ Hai esperienza con SQL/NOSQL e Python (Pandas, Numpy, Sklearn).\r\n✅ Conosci AWS (Athena, Redshift, S3) e tool di Data Visualization (Qlik Cloud, Tableau).\r\n✅ Sei proattivo e abituato a lavorare in team multifunzionali.\r\n\r\nNice to have:\r\nEsperienza in Advanced Analytics.\r\nConoscenza della Data Governance.\r\n\r\n🏡 Modalità ibrida.\r\n💰 Welfare aziendale",
    #     "questions": [
    #       "Hai maturato almeno 2 anni di esperienza nel ruolo?",
    #       "Sei disponibile a lavorare in modalità ibrida su Milano?"
    #     ],
    #     "open_questions": [
    #       "Racconta brevemente la tua esperienza come Data Analyst e quali tipi di tecnologie hai usato lato elaborazione dati e data visualization",
    #       " Come mai hai deciso di candidati per IlSole24Ore? Quali affinità vedi con il ruolo?"
    #     ],
    #     "uuid": "64efd203-ca9f-4f72-8b80-3d952b985202",
    #     "hr_email": [
    #       "anna.forte@ilsole24ore.com",
    #       ""
    #     ],
    #     "datapizza_manager_email": "gabriele@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "rec5K5oQPZKAZQfxY",
    #     "extra": {
    #       "role": "Data Analyst",
    #       "benefits": "Non specificati",
    #       "requisiti": "Laurea magistrale in ambito STEM, esperienza minima di 3-4 anni in aziende data-driven o in progetti di Advanced Analytics e Data Science, buona propensione alla comunicazione e capacità relazionali, attitudine analitica e orientamento al problem solving, buona conoscenza dell’inglese, proattività e flessibilità.",
    #       "work_model": "hybrid",
    #       "day_on_site": "3 Giorni/Settimana",
    #       "extra_skills": "",
    #       "schedule_type": "Full-Time",
    #       "extracted_text": "La risorsa sarà inserita all’interno dell’area Business Data Management ovvero della componente aziendale a supporto della digital trasformation che sta caratterizzando il Gruppo 24 ORE. Il ruolo prevede una forte connotazione tecnica in ambito analitico unita a capacità di generare valore dai dati. Principali responsabilità includono l'estrazione, analisi e interpretazione dei dati usando sorgenti dati multiple, sviluppo di report, targeting e valutazione quantitativo-statistica delle campagne di Marketing, e coinvolgimento nella progettualità di data-driven Strategy. Richiesta esperienza in progetti di Advanced Analytics e conoscenza di database relazionali e linguaggi SQL/NOSQL.",
    #       "additional_info": "",
    #       "responsabilities": "",
    #       "first_requirement": "",
    #       "selection_process": "Colloquio motivazionale e tecnico 1, colloquio motivazionale e tecnico 2 di approfondimento",
    #       "hiring_expectation": 1,
    #       "second_requirement": ""
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "true",
    #     "created_at": "2024-10-07T12:13:54+02:00",
    #     "updated_at": "2024-10-15T21:25:39.431480+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       28,
    #       37,
    #       42,
    #       48,
    #       99,
    #       129
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 227,
    #     "technologies": [
    #       {
    #         "id": 83,
    #         "uuid": "de7ba1f2-642b-4d92-81c6-c3e136969ad5",
    #         "skillname": "Kubernetes",
    #         "color": "gray",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 70,
    #         "uuid": "31b29625-d0be-49bd-84f1-c6ffe92ccbf7",
    #         "skillname": "Google Cloud",
    #         "color": "info",
    #         "category": "Cloud Provider"
    #       },
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 82,
    #         "uuid": "0d8fe1ea-2f78-4840-9ee1-f4bf685f000b",
    #         "skillname": "Docker",
    #         "color": "success",
    #         "category": "Tech Infrastructure"
    #       },
    #       {
    #         "id": 9,
    #         "uuid": "71589f85-70d1-46a6-ba2d-9cdfb5befb69",
    #         "skillname": "NodeJS",
    #         "color": "warning",
    #         "category": "Backend"
    #       }
    #     ],
    #     "company": {
    #       "name": "Syllotips",
    #       "tag": "Syllotips",
    #       "logo": "https://api.datapizza.tech/media/companies/fbbc090f-b5ab-48e1-9a50-019fd08aab1e/Syllo.jpeg"
    #     },
    #     "infos": [
    #       {
    #         "id": 25,
    #         "infoname": "Full Time",
    #         "color": "green",
    #         "category": "Contract"
    #       },
    #       {
    #         "id": 96,
    #         "infoname": "🚀 Stock Option Plan",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 235,
    #         "infoname": "💼 Esperienza 5+ Anni",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 269,
    #         "infoname": "🏠Remote con 1o2 giorni di presenza al mese",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 317,
    #         "infoname": "💸 RAL: 50k - 80k",
    #         "color": "blue",
    #         "category": "RAL"
    #       }
    #     ],
    #     "name": "Full Stack Engineer",
    #     "emoji": "🖥",
    #     "contract": "permanent",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Roma",
    #     "min_ral": 50,
    #     "min_ral_ext": 0,
    #     "max_ral": 80,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 4,
    #     "max_work_experience": 8,
    #     "min_role_experience": 0,
    #     "max_role_experience": 0,
    #     "description": "SylloTips è una startup che sta trasformando il modo in cui le aziende condividono conoscenza, grazie a un agente conversazionale avanzato.\r\n\r\nIl ruolo prevede:\r\n👉 Sviluppare backend con NodeJS e Typescript \r\n👉 Creare e migliorare funzionalità frontend in React \r\n👉 Definire e gestire pipeline DevOps con Kubernetes e Docker\r\n\r\nSei la persona giusta se:\r\n✅ 5+ anni di esperienza con Typescript, React, NodeJS \r\n✅ Esperienza nell'uso di Docker, Kubernetes \r\n✅ Familiarità con ambienti Cloud, Firebase ed Elastic Search \r\n\r\nNice to have: \r\n- Conoscenza di Python e strumenti di Data Science \r\n- Esperienza con architetture serverless\r\n\r\n🎓 Lauree in ambito STEM\r\n\r\nSi offrono:\r\n💼 Stock options \r\n🌍 Remote con 10 incontri in sede/anno a Roma \r\n\r\nIter di selezione: Colloquio HR + 2 Test Tecnici + Colloquio finale.",
    #     "questions": [
    #       "Hai almeno 4 anni di esperienza nelle tecnologie richieste NodeJS e Typescript e React?",
    #       "Hai familarità con Docker, Kubernetes e in generale con il ciclo DevOps",
    #       "Hai familiarità con gli ambienti Cloud?"
    #     ],
    #     "open_questions": [
    #       "Perché ritieni di essere in linea per questa posizione?",
    #       "Hai mai svolto progetti che integrassero AI?"
    #     ],
    #     "uuid": "2c76e1b8-2da1-45da-a5ba-be7552e55589",
    #     "hr_email": [],
    #     "datapizza_manager_email": "gabriele@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recXVnh9at7SdwLVB",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-09-11T15:41:34+02:00",
    #     "updated_at": "2024-10-16T15:25:45.598530+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       6,
    #       9,
    #       82
    #     ],
    #     "nice_to_have_technologies": [
    #       48,
    #       70,
    #       83
    #     ]
    #   },
    #   {
    #     "id": 78,
    #     "technologies": [
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 37,
    #         "uuid": "4b2d3e82-0fee-4c29-bddb-e7b59cfd9253",
    #         "skillname": "SQL",
    #         "color": "gray",
    #         "category": "Database"
    #       },
    #       {
    #         "id": 30,
    #         "uuid": "6e458e91-c4de-4a36-9926-73b03183ff61",
    #         "skillname": "QlikSense",
    #         "color": "indigo",
    #         "category": "Business Intelligence"
    #       },
    #       {
    #         "id": 28,
    #         "uuid": "81794b7a-9389-475d-9461-cc93f8bd5b82",
    #         "skillname": "PowerBI",
    #         "color": "success",
    #         "category": "Business Intelligence"
    #       }
    #     ],
    #     "company": {
    #       "name": "Praxi",
    #       "tag": "praxi",
    #       "logo": "https://api.datapizza.tech/media/companies/39564a7d-fd04-4759-9677-0574da6a98c1/zs9nPs98_400x400.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 1,
    #         "infoname": "💼 2-3 Years Experience",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 22,
    #         "infoname": "💸 RAL 35k-45k",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 102,
    #         "infoname": "Ibrido - Milano",
    #         "color": "red",
    #         "category": "Location"
    #       }
    #     ],
    #     "name": "Data Analyst",
    #     "emoji": "📈",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Milano",
    #     "min_ral": 0,
    #     "min_ral_extra": 0,
    #     "max_ral": 0,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 0,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "PRAXI Informatica, una divisione di PRAXI S.p.A., è alla ricerca di un Data Analyst appassionato di dati e tecnologia.\r\n\r\n✨ Le tue responsabilità:\r\n\r\n👉 Acquisire dati da DataBase gestionali, ambienti social, Big Data, IoT.\r\n👉 Preparare e analizzare i dati per scoprire correlazioni e pattern interpretativi, utilizzando anche algoritmi di Machine Learning\r\n👉 Predisporre reportistica per la presentazione dei risultati\r\n\r\nFa per te se:\r\n\r\n1. Possiedi una laurea in informatica o ingegneria informatica\r\n\r\n2. Conosci Qlik, Microsoft Power BI\r\n\r\n3. Sai rapportarti con un cliente e hai esperienza nel relazionarti e comunicare i risultati del tuo lavoro.\r\n\r\nLa sede è a Milano in Via Pagano. È richiesta la disponibilità a fare trasferte nel centro-nord.",
    #     "questions": [
    #       "Conosci Qlik, PowerBI, SQL e Python?",
    #       "Hai una laurea in Informatica o Ingegneria Informatica?",
    #       "Sei disponibile a lavorare su Milano e a fare molte trasferte per incontrare clienti?"
    #     ],
    #     "open_questions": [],
    #     "uuid": "2945cb12-6658-4777-91e9-00d4514f8656",
    #     "hr_email": [
    #       "andrea.delmonte@praxi.praxi"
    #     ],
    #     "datapizza_manager_email": "",
    #     "position_type": "success",
    #     "airtable_id": "reck6UerlWWQZFNZP",
    #     "extra": {},
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-01-22T11:47:36+01:00",
    #     "updated_at": "2024-09-03T21:46:28.727052+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       28,
    #       30,
    #       37,
    #       48
    #     ],
    #     "nice_to_have_technologies": []
    #   },
    #   {
    #     "id": 124,
    #     "technologies": [
    #       {
    #         "id": 6,
    #         "uuid": "d6cc0db8-b0e8-48c5-9d3a-8f3f373ed159",
    #         "skillname": "Typescript",
    #         "color": "gray",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 1,
    #         "uuid": "409192af-ab9f-4a56-a980-343e06b1817c",
    #         "skillname": "React",
    #         "color": "success",
    #         "category": "Frontend"
    #       },
    #       {
    #         "id": 48,
    #         "uuid": "cbe1ec6f-d503-4457-943b-ed0a11bbe484",
    #         "skillname": "Python",
    #         "color": "success",
    #         "category": "Coding"
    #       },
    #       {
    #         "id": 8,
    #         "uuid": "16d066ef-7cd4-46e7-bad1-7083eddb2195",
    #         "skillname": "Django",
    #         "color": "success",
    #         "category": "Backend"
    #       },
    #       {
    #         "id": 150,
    #         "uuid": "dab5c5cf-9259-4418-91f1-fe9d43e57559",
    #         "skillname": "Next.JS",
    #         "color": "red",
    #         "category": "Frontend"
    #       }
    #     ],
    #     "company": {
    #       "name": "Datapizza",
    #       "tag": "datapizza",
    #       "logo": "https://api.datapizza.tech/media/companies/4fb78fca-f6fb-487a-8e22-9a0edea6e2ad/channels4_profile.jpg"
    #     },
    #     "infos": [
    #       {
    #         "id": 73,
    #         "infoname": "🌎 Full Remote",
    #         "color": "red",
    #         "category": "Location"
    #       },
    #       {
    #         "id": 93,
    #         "infoname": "🧑‍💻 1-2 Years Experience",
    #         "color": "yellow",
    #         "category": "Experience"
    #       },
    #       {
    #         "id": 96,
    #         "infoname": "🚀 Stock Option Plan",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 135,
    #         "infoname": "💸 25k - 30k RAL",
    #         "color": "blue",
    #         "category": "RAL"
    #       },
    #       {
    #         "id": 138,
    #         "infoname": "🏖️ Retreat fighissimi",
    #         "color": "indigo",
    #         "category": "Other"
    #       },
    #       {
    #         "id": 173,
    #         "infoname": "💸 Buoni pasto ~ 2k anno",
    #         "color": "indigo",
    #         "category": "Other"
    #       }
    #     ],
    #     "name": "Frontend Developer Jr",
    #     "emoji": "🍕",
    #     "contract": "",
    #     "contract_extra": "",
    #     "schedule": "full_time",
    #     "location": "Remote",
    #     "min_ral": 25000,
    #     "min_ral_extra": 0,
    #     "max_ral": 30000,
    #     "max_ral_extra": 0,
    #     "min_work_experience": 0,
    #     "max_work_experience": 20,
    #     "min_role_experience": 0,
    #     "max_role_experience": 20,
    #     "description": "Vuoi entrare a far parte del Team di Datapizza? 🍕\r\n\r\nSiamo alla ricerca di una nuo va aggiunta al nostro team, per ricoprire il ruolo di Software Engineer: 70% Frontend - 30% Backend.\r\nTi occuperai di aiutarci nello sviluppo della piattaforma su cui ti stai candidando e di altre cose fighissime.\r\n\r\nMa che caratteristiche ha la figura che stiamo cercando?\r\n\r\n💎 Ha esperienza nello sviluppo Frontend.\r\n🧱 Non ha paura di sporcarsi le mani con il Backend.\r\n🐳 Se parla di container non si riferisce alle spedizioni.\r\n\r\nQuesta opportunità fa per te se:\r\n\r\n🫡 Hai voglia di fare la differenza.\r\n🚀 Vuoi far parte di una startup vivace contribuendo attivamente al progetto Datapizza.\r\n\r\nProcesso di selezione:\r\n✅ Test tecnico (Django + React)\r\n✅ Colloquio tecnico\r\n✅ Colloquio Attitudinale",
    #     "questions": [
    #       "Ti ritieni più improntato al Frontend rispetto che al Backend?",
    #       "Sei aperto a una collaborazione Full Time a lungo termine?",
    #       "Sei pronto a lavorare in un team giovane in startup?"
    #     ],
    #     "open_questions": [
    #       "Perché ti ritieni in grado di sviluppare in React e Django?",
    #       "Hai interesse o praticità in ambito UX/UI ?",
    #       "Dovendo auto valutare le tue skill in Typescript come ti descriveresti?",
    #       "Scrivi qui sotto una breve presentazione di te in termini di educazione, esperienza e obiettivi di carriera"
    #     ],
    #     "uuid": "126240e3-1e0b-4b1b-9a1d-d3f3ccf9b027",
    #     "hr_email": [
    #       "davide@datapizza.tech",
    #       "",
    #       "",
    #       ""
    #     ],
    #     "datapizza_manager_email": "gabriella@datapizza.tech",
    #     "position_type": "success",
    #     "airtable_id": "recXq2RCKiTY6HvNo",
    #     "extra": {
    #       "role": "softwareengineer",
    #       "benefits": "Retreat Aziendali fighissimi Incentivi alla formazione",
    #       "contract": "Permanent Contract",
    #       "day_on_site": 0,
    #       "extra_skills": "",
    #       "additional_info": "",
    #       "responsabilities": "Vuoi entrare a far parte del Team di Datapizza? 🍕\nMa che caratteristiche ha la figura che stiamo cercando?\n\n💎 Ha esperienza nello sviluppo Frontend.\n🧱 Non ha paura di sporcarsi le mani con il Backend.\n🐳 Se parla di container non si riferisce alle spedizioni.",
    #       "first_requirement": "Typescript",
    #       "selection_process": "Test tecnico \nColloquio tecnico\nColloquio Motivazionale",
    #       "hiring_expectation": "1",
    #       "second_requirement": "Python"
    #     },
    #     "airtable_share_id": "",
    #     "pdf_conversion": "false",
    #     "created_at": "2024-04-24T11:47:36+02:00",
    #     "updated_at": "2024-10-18T10:47:44.719326+02:00",
    #     "status": "active",
    #     "datapizza_hr_notes": "",
    #     "must_have_technologies": [
    #       1,
    #       6,
    #       8,
    #       48
    #     ],
    #     "nice_to_have_technologies": [
    #       150
    #     ]
    #   }
    # ]
