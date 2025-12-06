--
-- PostgreSQL database dump
--

-- Dumped from database version 15.12 (Debian 15.12-1.pgdg120+1)
-- Dumped by pg_dump version 15.12 (Debian 15.12-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.alembic_version (version_num) FROM stdin;
e3498f5c23c3
\.


--
-- Data for Name: types; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.types (id, libelle, description, created_at) FROM stdin;
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.events (id, name, url, description, date_debut, date_fin, created_at, ville, adresse, code_postal, type_id) FROM stdin;
\.


--
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.images (id, url, description, created_at, event_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.users (id, name, email, mdp, role, created_at, google_id) FROM stdin;
3	test	test@test.com	$2b$12$OG9FUHg6/OEN4SMj1zDCZu5a9MVDxwcf/KDn3D9Ve/bt4Bu6ZXVq6	user	2025-12-05 09:21:28.73197	\N
\.


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.events_id_seq', 1, false);


--
-- Name: images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.images_id_seq', 1, false);


--
-- Name: types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.types_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

