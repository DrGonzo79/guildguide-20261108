import fixtures from "../data/demo.json";
export type GuideRequest={communityId:string;useCase:string;budget:number;maxAgeDays:number};
export type Pick={id:string;name:string;price:number;score:number;fit:number;confidence:number;freshness:"current"|"review";source:string;dissent:string;why:string};
export type GuideResult={communityName:string;expert:string;picks:Pick[];queue:{id:string;name:string;reason:string}[];ruleVersion:string};
export const communities=fixtures.communities;
export function generateGuide(request:GuideRequest):GuideResult{
  const community=fixtures.communities.find(item=>item.id===request.communityId);
  if(!community)throw new Error("Choose a known demo community.");
  if(!community.useCases.includes(request.useCase))throw new Error("Choose a use case supported by this community.");
  if(!Number.isFinite(request.budget)||request.budget<100||request.budget>20000)throw new Error("Budget must be between $100 and $20,000.");
  if(request.maxAgeDays<30||request.maxAgeDays>730)throw new Error("Review age must be between 30 and 730 days.");
  const products=fixtures.products.filter(item=>item.communityId===request.communityId&&item.price<=request.budget&&item.useCases.includes(request.useCase));
  const picks=products.map(item=>{
    const freshness=item.reviewedDaysAgo<=request.maxAgeDays?"current" as const:"review" as const;
    const ageScore=Math.max(0,100-item.reviewedDaysAgo/3);
    const score=Math.round(item.fit*.5+item.confidence*.3+ageScore*.2);
    return {...item,score,freshness,why:`${item.fit}% expert fit · ${item.confidence}% community confidence · reviewed ${item.reviewedDaysAgo} days ago`};
  }).sort((a,b)=>b.score-a.score);
  const queue=fixtures.products.filter(item=>item.communityId===request.communityId&&(item.reviewedDaysAgo>request.maxAgeDays||item.confidence<70)).map(item=>({id:item.id,name:item.name,reason:item.reviewedDaysAgo>request.maxAgeDays?`Evidence is ${item.reviewedDaysAgo} days old`:`Confidence is only ${item.confidence}%`}));
  return {communityName:community.name,expert:community.expert,picks,queue,ruleVersion:"2026.11.08"};
}
