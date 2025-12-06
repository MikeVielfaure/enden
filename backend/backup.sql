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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO mike;

--
-- Name: events; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.events (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    url character varying(500),
    description character varying(1000),
    date_debut timestamp without time zone NOT NULL,
    date_fin timestamp without time zone NOT NULL,
    created_at timestamp without time zone,
    ville character varying(100) NOT NULL,
    adresse character varying(200),
    code_postal character varying(5),
    type_id integer NOT NULL
);


ALTER TABLE public.events OWNER TO mike;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO mike;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: images; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.images (
    id integer NOT NULL,
    url character varying(500) NOT NULL,
    description character varying(500),
    created_at timestamp without time zone,
    event_id integer NOT NULL
);


ALTER TABLE public.images OWNER TO mike;

--
-- Name: images_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_id_seq OWNER TO mike;

--
-- Name: images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.images_id_seq OWNED BY public.images.id;


--
-- Name: types; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.types (
    id integer NOT NULL,
    libelle character varying(255) NOT NULL,
    description character varying(500),
    created_at timestamp without time zone
);


ALTER TABLE public.types OWNER TO mike;

--
-- Name: types_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.types_id_seq OWNER TO mike;

--
-- Name: types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.types_id_seq OWNED BY public.types.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying,
    email character varying,
    mdp character varying,
    role character varying,
    created_at timestamp without time zone,
    google_id character varying
);


ALTER TABLE public.users OWNER TO mike;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO mike;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: images id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.images ALTER COLUMN id SET DEFAULT nextval('public.images_id_seq'::regclass);


--
-- Name: types id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.types ALTER COLUMN id SET DEFAULT nextval('public.types_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.alembic_version (version_num) FROM stdin;
e3498f5c23c3
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
-- Data for Name: types; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.types (id, libelle, description, created_at) FROM stdin;
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
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: images images_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);


--
-- Name: images images_url_key; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_url_key UNIQUE (url);


--
-- Name: types types_libelle_key; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.types
    ADD CONSTRAINT types_libelle_key UNIQUE (libelle);


--
-- Name: types types_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.types
    ADD CONSTRAINT types_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: mike
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_google_id; Type: INDEX; Schema: public; Owner: mike
--

CREATE UNIQUE INDEX ix_users_google_id ON public.users USING btree (google_id);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: mike
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_users_name; Type: INDEX; Schema: public; Owner: mike
--

CREATE INDEX ix_users_name ON public.users USING btree (name);


--
-- Name: events events_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_type_id_fkey FOREIGN KEY (type_id) REFERENCES public.types(id);


--
-- Name: images images_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

