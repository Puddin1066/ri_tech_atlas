import type { NextConfig } from "next";

/** Production on bioticabio.com/ri-life-science-atlas (see bioticabio vercel rewrites). */
const basePath =
  process.env.ATLAS_BASE_PATH ??
  (process.env.VERCEL === "1" ? "/ri-life-science-atlas" : "");

const nextConfig: NextConfig = {
  ...(basePath ? { basePath, assetPrefix: basePath } : {}),
  experimental: {
    externalDir: true,
  },
};

export default nextConfig;
