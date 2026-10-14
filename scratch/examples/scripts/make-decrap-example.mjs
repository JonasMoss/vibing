// Generates a SYNTHETIC WISEflow-style grading export for the Day-1 decrap exercise.
// Fake IDs, placeholder file contents — safe to commit and hand out. Reproducible:
// edit the `subs` table and re-run `node scratch/examples/scripts/make-decrap-example.mjs`.
//
// The mess it recreates (modelled on a real WISEflow download, kept private;
// every ID and file name below is invented, none is copied from it):
//   - every submission folder is `[N-1234567] - Group GG` — three numbers, and the
//     one you grade by (Group) is last and scattered;
//   - it sorts by N *as text*, so [1],[10],[11]…[15],[2],[3]… — chaos;
//   - the real work is buried in a nested "Appendix material" folder under names
//     every group invented themselves.
// The target the exercise produces: a flat folder of `NN-report.pdf` + `NN-report.pbix`.

import { mkdir, writeFile, rm } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const root = fileURLToPath(new URL("../../", import.meta.url));
const OUT = join(root, "examples", "decrap-me");

// [submissionNumber, wiseflowId, group, pbixName, reportName]  — names deliberately awful.
const subs = [
  [1, 2031847, 5, "NordicStyle_dashbord_final.pbix", "BI_exam_group5.docx"],
  [2, 2056310, 12, "EKSAMEN.pbix", "EKSAMEN.pdf"],
  [3, 2048892, 1, "eksamen_v4.pbix", "bizreport_FINAL.pdf"],
  [4, 2062175, 9, "PowerBI_exam_v1.pbix", "Report.pdf"],
  [5, 2039468, 15, "sales_dash.pbix", "final_project_report_PBI.pdf"],
  [6, 2071933, 3, "nordicstyle-pbi.pbix", "report.docx"],
  [7, 2044106, 11, "examTHISONE.pbix", "appendix_tech.pdf"],
  [8, 2059527, 7, "powerbi_exam_2025.pbix", "rapport.pdf"],
  [9, 2067741, 2, "PBI_eksamen.pbix", "exam (1).pdf"],
  [10, 2035284, 14, "BIreport.pbix", "Report_FINAL_v2_fixed.docx"],
  [11, 2052619, 6, "assignment.pbix", "business_report_g6.docx"],
  [12, 2049370, 4, "dashboard_v3_FINAL.pbix", "group_report_final.docx"],
  [13, 2063058, 13, "Power BI Report.pbix", "analysis.pdf"],
  [14, 2040715, 8, "final.pbix", "ELE37911_group8.pdf"],
  [15, 2074406, 10, "NS_dashboard(2).pbix", "rapport_endelig.pdf"],
];

const reportText = (group) => `Nordic Style — Business Intelligence exam (ELE37911)
Group ${group}

Executive summary
-----------------
This report analyses Nordic Style's campaign performance across sales channels
using the provided Power BI model (Customers, Products, Campaigns, ChannelMap).

Key findings
------------
- Channel mix shifted toward online over the period.
- The spring campaign returned the highest revenue per customer.
- Two product categories account for most of the margin.

(Placeholder content for the course exercise — not a real submission.)
`;

const pbixText = (group) =>
  `PBIX-PLACEHOLDER  Nordic Style dashboard — Group ${group}.\n` +
  `Stand-in for a binary Power BI file; contents irrelevant to the decrap.\n`;

const coverText = (n, id, group) =>
  `WISEflow cover sheet\nSubmission ${n} · participant ${id} · Group ${group}\n` +
  `ELE37911 Business Intelligence with Power BI\n`;

await rm(OUT, { recursive: true, force: true });

// Shared, top-level material — these should be LEFT ALONE, not reshuffled (a nice trap).
await mkdir(join(OUT, "Assignment"), { recursive: true });
await writeFile(join(OUT, "Assignment", "Customers.csv"), "customer_id,name,segment,city\n1,Placeholder,Retail,Oslo\n2,Placeholder,Online,Bergen\n");
await writeFile(join(OUT, "Assignment", "Products.csv"), "product_id,category,price\n1,Jackets,1200\n2,Boots,900\n");
await writeFile(join(OUT, "Assignment", "Campaigns.csv"), "campaign_id,season,budget\n1,Spring,50000\n2,Autumn,40000\n");
await writeFile(join(OUT, "Assignment", "ChannelMap.csv"), "channel_id,channel\n1,Online\n2,Retail\n");
await writeFile(join(OUT, "Assignment", "ELE37911.pdf"), "ELE37911 — exam brief (placeholder). Build a Power BI report for Nordic Style.\n");
await mkdir(join(OUT, "Marking guidance"), { recursive: true });
await writeFile(join(OUT, "Marking guidance", "solution_guide_ELE37911.pdf"), "Solution guide (placeholder). Grade by group; expected KPIs listed here.\n");
await writeFile(join(OUT, "Grade-sheet-[7318204]-[ELE-37911-Business-Intelligence-with-Power-BI].csv"), "Group,Mark\n" + subs.map((s) => `${s[2]},`).join("\n") + "\n");
await writeFile(join(OUT, "_METADATA"), "Synthetic WISEflow-style export for the decrap exercise. Fake IDs, placeholder files.\n");

// Submissions — the actual horror.
const duplicateBody = reportText("(shared template)"); // groups 1 & 2 hand in byte-identical reports
for (const [n, id, group, pbix, report] of subs) {
  const dir = join(OUT, "Submissions", `[${n}-${id}] - Group ${group}`);
  const appendix = join(dir, "Appendix material");
  await mkdir(appendix, { recursive: true });
  await writeFile(join(dir, "Cover sheet.pdf"), coverText(n, id, group));
  await writeFile(join(appendix, pbix), pbixText(group));
  const body = group === 1 || group === 2 ? duplicateBody : reportText(group);
  await writeFile(join(appendix, report), body);
}

console.log(`Built synthetic decrap example at examples/decrap-me (${subs.length} groups).`);

// The handout and the schedule both say "everyone downloads decrap-me.zip", so emit it
// here rather than by hand — a zip built separately WILL drift from the folder.
// Zipped from examples/ so it unpacks as a `decrap-me/` folder, not 40 loose files
// into whatever directory a participant happens to be standing in.
const execFileAsync = promisify(execFile);
const zipPath = join(root, "examples", "decrap-me.zip");
await rm(zipPath, { force: true });
try {
  await execFileAsync("zip", ["-r", "-q", "decrap-me.zip", "decrap-me"], {
    cwd: join(root, "examples"),
  });
  console.log("Wrote examples/decrap-me.zip");
} catch (err) {
  console.error(
    `\n!! Could not build examples/decrap-me.zip: ${err.message}\n` +
      `   Install 'zip', or make it by hand from examples/:  zip -r decrap-me.zip decrap-me\n` +
      `   Day 1 13:00 hands this file out — do not skip it.\n`,
  );
  process.exitCode = 1;
}
