# Mayank.dev

Personal portfolio and Kubernetes engineering blog for Mayank Yadav, a Platform and DevOps Engineer
focused on Kubernetes, Terraform, cloud infrastructure, GitOps, delivery automation, reliability, and
security.

The repository contains a dependency-free static website published through GitHub Pages. It is designed
to present production-focused platform engineering work, detailed case studies, technical focus areas,
and practical Kubernetes articles without requiring a frontend framework, build system, or package
manager.

## Live Site

- Portfolio: [https://sremayank.github.io/](https://sremayank.github.io/)
- Kubernetes blog: [https://sremayank.github.io/blog/index.html](https://sremayank.github.io/blog/index.html)
- GitHub profile: [https://github.com/sremayank](https://github.com/sremayank)
- LinkedIn: [https://www.linkedin.com/in/mayank-k-yadav/](https://www.linkedin.com/in/mayank-k-yadav/)

## What the Site Contains

### Portfolio

The main portfolio page introduces Mayank's platform engineering background and highlights experience
across AWS, GCP, Kubernetes, Terraform, CI/CD, GitOps, autoscaling, security guardrails, and operational
automation.

Its primary sections are:

- **Hero and engineering profile**: specialisms, technology badges, experience metrics, and calls to action.
- **Featured case studies**: detailed examples of multi-cluster GKE modernisation, KEDA-based autoscaling,
  and serverless GKE cost optimisation.
- **More work**: GitOps delivery, ArgoCD drift detection, SlackOps, and infrastructure supply-chain
  hardening.
- **Focus areas**: cloud platform engineering, Kubernetes reliability, delivery automation, and operational
  guardrails.
- **Interactive content roadmap**: a placeholder for future visual architecture walkthroughs.
- **Kubernetes blog preview**: selected technical articles linked from the portfolio.
- **Contact section**: GitHub, LinkedIn, and email links.

Featured case studies use keyboard-aware modal dialogs implemented with lightweight, framework-free
JavaScript and ARIA labeling. Modals can be opened from case-study cards and closed using the close
button, backdrop, or Escape key.

### Kubernetes Blog

The blog contains detailed operational guides written for engineers running Kubernetes in
production-style environments. Articles combine explanations, architecture diagrams, example manifests,
commands, troubleshooting workflows, and production checklists.

Current topics include:

- Tracing traffic from external load balancers and Service virtual IPs to Pods
- Building defense in depth across Kubernetes cluster layers
- Designing reliable multi-container Pods with sidecars
- Troubleshooting unhealthy DaemonSets
- Managing Pods with Deployments and Services
- Connecting Pods to persistent storage
- Protecting workloads with namespaces and namespace-scoped controls
- Exposing applications with Kubernetes Services
- Fixing `OOMKilled` and `ImagePullBackOff`
- Understanding Kubernetes memory limits and OOM behavior

## Technology and Design

This site deliberately uses a small and transparent technology stack:

- Semantic HTML5
- Modern CSS with responsive layouts and CSS custom properties
- Vanilla JavaScript for portfolio case-study modals
- Google Fonts using the Inter typeface
- GitHub Pages for static hosting and deployment

There are no runtime dependencies, generated assets, package-lock files, or build commands. Every page
can be opened directly or served by a basic local HTTP server.

The visual system uses a dark platform-engineering theme with:

- Responsive card grids
- Sticky navigation
- Reusable color, spacing, radius, and shadow variables
- Mobile breakpoints
- Styled command, YAML, and architecture-diagram blocks
- Clear article callouts, metadata, and table-of-contents navigation

## Repository Structure

```text
.
├── index.html
├── README.md
├── .gitignore
└── blog/
    ├── index.html
    ├── styles.css
    ├── building-security-into-every-layer-of-a-kubernetes-cluster.html
    ├── designing-reliable-multi-container-pods-with-kubernetes-sidecars.html
    ├── from-service-vip-to-pod-tracing-traffic-through-kubernetes.html
    ├── how-to-connect-kubernetes-pods-to-persistent-storage.html
    ├── how-to-fix-oomkilled-and-imagepullbackoff-in-kubernetes.html
    ├── how-to-protect-kubernetes-using-namespaces.html
    ├── how-to-troubleshoot-unhealthy-kubernetes-daemonsets.html
    ├── how-to-use-kubernetes-deployments-and-services-to-manage-pods.html
    ├── how-to-use-kubernetes-service-to-expose-your-application.html
    └── understanding-kubernetes-oomkilled.html
```

### Important Files

- `index.html`: the complete portfolio page, including its CSS, content, modal markup, and JavaScript.
- `blog/index.html`: the blog landing page and article-card catalog.
- `blog/styles.css`: shared styling for the blog index and all standalone articles.
- `blog/*.html`: self-contained technical articles that use the shared blog stylesheet.

## Run Locally

Clone the repository and start a local static server:

```bash
git clone https://github.com/sremayank/sremayank.github.io.git
cd sremayank.github.io
python3 -m http.server 8000
```

Open:

- Portfolio: [http://localhost:8000/](http://localhost:8000/)
- Blog: [http://localhost:8000/blog/index.html](http://localhost:8000/blog/index.html)

Press `Ctrl+C` to stop the server.

Opening HTML files directly can work for simple checks, but using an HTTP server provides behavior closer
to GitHub Pages and makes link verification easier.

## Updating Portfolio Content

The portfolio is maintained directly in `index.html`.

When adding or changing a case study:

1. Update or add the case-study card in the appropriate section.
2. Add a corresponding detail modal when the case study needs a deeper explanation.
3. Give the trigger a `data-modal-target` matching the modal `id`.
4. Keep modal labels and controls accessible with `aria-labelledby`, `aria-label`, and semantic headings.
5. Verify the modal opens, closes, returns focus, closes on backdrop click, and closes with Escape.

When updating navigation or contact information, check both the portfolio and blog pages so links remain
consistent across the whole site.

## Adding a Blog Article

Blog articles are standalone HTML files in `blog/`. Use an existing detailed article as the starting
structure and retain the shared navigation, stylesheet, and footer.

A complete article should include:

- A unique and descriptive page title
- An accurate meta description
- An original article headline
- An eyebrow category, publication date, read time, and Kubernetes tag
- A concise introductory callout
- A table of contents with working section anchors
- Practical explanations, commands, manifests, or architecture diagrams
- Operational tradeoffs and troubleshooting guidance
- A production checklist or concluding mental model
- A back link to the blog index

After creating the article:

1. Add a card to `blog/index.html`.
2. Confirm the article filename and card link match exactly.
3. Verify every table-of-contents link points to an existing section ID.
4. Check long commands and diagrams for horizontal overflow.
5. Review technical examples for safe production guidance.

## Validation

Because the site has no build step, validation focuses on markup, links, layout, and browser behavior.

Run a whitespace and patch-quality check:

```bash
git diff --check
```

Find Blog navigation links:

```bash
rg -n '<a href="[^"]+">Blog</a>' --glob '*.html'
```

Check that every article linked from the blog index exists:

```bash
for link in $(rg -o 'href="\./[^"#]+"' blog/index.html | cut -d'"' -f2); do
  test -f "blog/${link#./}" || echo "Missing: $link"
done
```

Before publishing, visually verify:

- Desktop and mobile layouts
- Portfolio navigation and contact links
- Case-study modal behavior
- Blog card links
- Article table-of-contents anchors
- Code-block scrolling
- No unexpected horizontal page overflow

## Deployment

GitHub Pages publishes the repository from the root of the `main` branch.

The normal publishing workflow is:

1. Create a feature branch.
2. Make and validate the changes locally.
3. Commit and push the branch.
4. Open a pull request into `main`.
5. Merge the pull request after review.
6. Wait for the GitHub Pages build and deployment workflow to complete.
7. Verify the change on the live site.

Changes pushed only to a feature branch do not appear on the public site. They become live after the
branch is merged into `main` and GitHub Pages completes deployment. Browser or CDN caching can briefly
show an older version after a successful deployment.

## Content Principles

The site aims to keep its technical content:

- Practical and production-oriented
- Clear about tradeoffs and failure modes
- Accurate about Kubernetes security and operational boundaries
- Useful during real troubleshooting
- Easy to navigate without unnecessary frontend complexity
- Consistent in visual design and article structure

## Contact

For platform engineering, DevOps, Kubernetes, cloud infrastructure, automation, or reliability
discussions:

- LinkedIn: [Mayank K Yadav](https://www.linkedin.com/in/mayank-k-yadav/)
- GitHub: [sremayank](https://github.com/sremayank)
- Email: [mayankkumaryadav01@gmail.com](mailto:mayankkumaryadav01@gmail.com)
