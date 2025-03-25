create table
  public.products_v2 (
    id uuid not null default gen_random_uuid (),
    attractiveness public.attractiveness_enum null,
    organization text not null,
    store uuid not null,
    seller uuid null,
    "size" text null,
    "category" text null,
    price numeric null,
    status public.product_status_enum null default 'active'::product_status_enum,
    materials text[] null,
    brand text null,
    seller_share numeric null,
    colors text[] null,
    sku numeric null,
    deleted boolean not null default false,
    sys_retrigger timestamp with time zone null,
    gender public.products_genders null,
    created timestamp with time zone null default now(),
    modified timestamp with time zone null default now(),
    pick_up timestamp with time zone null,
    expired timestamp with time zone null,
    donated timestamp with time zone null,
    stolen timestamp with time zone null,
    purchased timestamp with time zone null,
    sold timestamp with time zone null,
    media jsonb[] null,
    constraint products_v2_pkey primary key (id),
    constraint products_v2_organization_fkey foreign key (organization) references organizations (organization_slug) on update cascade on delete cascade,
    constraint products_v2_store_id_fkey foreign key (store) references stores (id) on update cascade on delete set null,
    constraint products_v2_seller_fkey foreign key (seller) references sellers (id) on update cascade on delete set null,
    constraint seller_share_check check (
      (
        (seller_share >= (0)::numeric)
        and (seller_share <= (1)::numeric)
      )
    )
  ) tablespace pg_default;

create index if not exists idx_products_v2_created on public.products_v2 using btree (created) tablespace pg_default;

create index if not exists idx_products_v2_organization on public.products_v2 using btree (organization) tablespace pg_default;

create index if not exists idx_products_v2_organization_created on public.products_v2 using btree (organization, created) tablespace pg_default;

create index if not exists idx_products_v2_organization_modified on public.products_v2 using btree (organization, modified) tablespace pg_default;

create index if not exists idx_products_v2_seller on public.products_v2 using btree (seller) tablespace pg_default
where
  (seller is not null);

create trigger generate_sku before insert on products_v2 for each row when (new.sku is null)
execute function increment_sku_counter ();

create trigger integrations_extenda_go_products
after insert
or
update on products_v2 for each row
execute function supabase_functions.http_request (
  'https://getcircular.ai/api/platform/integrations/extenda-go/products',
  'POST',
  '{"Content-type":"application/json"}',
  '{}',
  '5000'
);

create trigger "product-db-webhook - review"
after insert
or
update on products_v2 for each row
execute function supabase_functions.http_request (
  'https://getcircular.ai/api/pub/product-db-webhook/products',
  'POST',
  '{"Content-type":"application/json"}',
  '{}',
  '5000'
);

create trigger "product-db-webhook"
after insert
or
update on products_v2 for each row
execute function supabase_functions.http_request (
  'https://getcircular.ai/api/pub/product-db-webhook/products',
  'POST',
  '{"Content-type":"application/json"}',
  '{}',
  '5000'
);

create trigger product_keywords_trigger
after insert
or
update on products_v2 for each row
execute function handle_product_keywords ();

create trigger testing
after insert
or
update on products_v2 for each row
execute function supabase_functions.http_request (
  'https://kalt.requestcatcher.com',
  'POST',
  '{"Content-type":"application/json"}',
  '{}',
  '5000'
);