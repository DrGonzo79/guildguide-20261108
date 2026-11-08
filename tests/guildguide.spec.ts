import {expect,test} from "@playwright/test";

test("generates a cited guide and flags a review",async({page})=>{
  await page.goto("/",{waitUntil:"networkidle"});
  await page.getByRole("button",{name:/Build maintained guide/}).click();
  await expect(page.getByText("Lumina X4")).toBeVisible();
  await page.getByRole("button",{name:"Inspect evidence →"}).first().click();
  await expect(page.getByText(/Member thread #482/)).toBeVisible();
  await page.getByRole("button",{name:"Flag for expert review"}).click();
  await expect(page.getByText("Member requested expert review")).toBeVisible();
});

test("shows an honest empty state and recovers",async({page})=>{
  await page.goto("/",{waitUntil:"networkidle"});
  await page.getByLabel("Use case").selectOption("portrait");
  await page.getByLabel("Maximum budget").fill("100");
  await page.getByRole("button",{name:/Build maintained guide/}).click();
  await expect(page.getByRole("heading",{name:"No eligible recommendation"})).toBeVisible();
  await page.getByLabel("Maximum budget").fill("2000");
  await page.getByRole("button",{name:/Build maintained guide/}).click();
  await expect(page.getByRole("heading",{name:"Portrait Pro 8"})).toBeVisible();
});

test("has no horizontal overflow",async({page})=>{
  await page.goto("/",{waitUntil:"networkidle"});
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>document.documentElement.clientWidth);
  expect(overflow).toBeFalsy();
});
