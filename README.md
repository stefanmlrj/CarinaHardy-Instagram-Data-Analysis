# Instagram Engagement Analysis

This repository contains an in-depth analysis of Instagram post performance data. The primary goal of this project is to uncover insights about **user engagement**—including **likes**, **comments**, **saves**, and overall **engagement rates**—and to identify factors that influence high-performing content. By leveraging data-driven strategies, this analysis aims to help optimize posting schedules and content strategies to maximize engagement.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup](#setup)
- [Analysis Process](#analysis-process)
- [Findings & Insights](#findings--insights)
- [Suggestions & Recommendations](#suggestions--recommendations)
- [Future Development](#future-development)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The project starts by cleaning and processing Instagram post data, which includes flattening JSON data into a usable format and calculating key engagement metrics like **likes**, **comments**, **reach**, **followers**, and **engagement rate**. After preparing the data, the analysis focuses on segmenting posts based on their performance—**high**, **medium**, and **low**—and uncovering patterns related to **timing**, **content type**, and **audience behavior**.

The ultimate goal is to provide actionable insights that can help Instagram account managers, content creators, and marketers improve their social media strategies.

---

## Setup

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/instagram-engagement-analysis.git
cd instagram-engagement-analysis
````

### Dependencies:

* **Python 3.x**
* `pandas`
* `matplotlib`
* `seaborn`
* `numpy`
* `scipy`
* `jupyter` (for notebook usage)

You can install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

---

## Analysis Process

1. **Data Cleaning and Preparation**:

   * The raw Instagram data, provided in JSON format, is flattened and cleaned. Missing values are handled, and engagement metrics such as **engagement rate** are recalculated.
   * Timestamps are converted into a local timezone to ensure time-based analysis is accurate.

2. **Segmentation**:

   * Posts are segmented into **high**, **medium**, and **low** performance categories based on **log-transformed engagement rates** to account for the skew in engagement data.




3. **Exploratory Data Analysis**:

   * The analysis includes visualizations of engagement by **hour of day**, **day of week**, and **month**, as well as relationships between **profile visits**, **follows**, **saves**, and engagement.


4. **Insights & Recommendations**:

   * The analysis identifies key trends such as peak engagement times, the correlation between profile visits and engagement, and the importance of saves in determining content success.

---

## Findings & Insights

* **Engagement by Day of the Week: When to Post for Maximum Impact**:

  * When analyzing the day of the week, I found that Fridays generally saw the highest average engagement across all posts. This suggests that users tend to be more active on Instagram towards the end of the workweek—likely as they relax and browse social media after a busy week. However, when I focused specifically on high-performing posts, Saturdays stood out as the top day for engagement.
  * It makes sense—on weekends, especially Saturdays, people have more free time to engage with content. With fewer obligations, users have the chance to interact more deeply with posts. This makes Saturdays the optimal day for posting content that you want to perform well.
  * Interestingly, Monday and Friday also showed strong engagement, indicating that the beginning and end of the week are key moments when users are active on Instagram. Even though Saturdays lead the pack, there’s still good engagement on these other weekdays.
  
  ![Average Engagement by Day of Week](insta-Project/data/source_data/processed/avg_engagement_by_day_of_week.png)
  ![HPP Engagement by Day](insta-Project/data/source_data/processed/HPP_engagement_by_day.png)

* **Engagement by Hour of the Day: Timing Is Everything**:

  * Timing your posts also plays a huge role in how well they perform. When I looked at engagement by hour of the day, I found that posts published in the morning—specifically between 8 AM and 10 AM—tended to get the most interaction. After that, engagement gradually dropped off throughout the day.
    This suggests that people are most active early in the morning before they get busy with the rest of their day. If you want to maximize your post’s visibility and engagement, morning posts are your best bet.
    
    ![Average Engagement by Hour of Day](insta-Project/data/source_data/processed/average_engagement_by_hour_of_day.png)
    ![HPP Engagement by Hour](insta-Project/data/source_data/processed/HPP_engagement_by_hour.png)

* **Engagement rate by Month and seeing the distribution of it**:
   * The monthly trend shows a clear decline in engagement from March through the end of the year. The early months, particularly March, captured strong audience interest, but engagement steadily weakened afterward, suggesting that the content might not have maintained the same level of resonance or consistency as the year progressed.
   
   ![Engagement Rate Log Transformed](insta-Project/data/source_data/processed/engagement_rate_log_transformed.png)

   ![Monthly Total Engagement](insta-Project/data/source_data/processed/monthly_total_engagement.png)
   ![HPP Monthly Total Engagement](insta-Project/data/source_data/processed/HPP_monthly_total_engagement.png)

* **Saves: An Indicator of Content Value**:

  * One of the most interesting findings was how saves correlate with engagement. Posts that were saved by users tended to see higher overall engagement. This suggests that saves are a great indicator of content value—if people are saving your posts, they’re finding them useful or interesting enough to come back to later.Encouraging users to save your posts could help boost long-term engagement. Creating content that’s informative, shareable, or particularly valuable to your audience is key to getting those saves and increasing interactions in the future.
  
  ![Saves vs Engagement Rate](insta-Project/data/source_data/processed/saves_vs_engagement_rate.png)

  ### Compare to other metrics, saves are the leading indicator for engagement rate
  ![Profile Visits vs Engagement Rate](insta-Project/data/source_data/processed/profile_visits_vs_engagement_rate.png)
  ![Follow vs Engagement Rate](insta-Project/data/source_data/processed/follow_vs_engagement_rate.png)

* **Medium-Performing Posts: An Opportunity for Growth**:

  * Most of the posts I analyzed fell into the medium-performing category. These posts performed decently, but there’s definitely room for improvement. The good news is that there’s a big opportunity to turn medium-performing posts into high-performing ones.
  By analyzing what makes high-performing posts successful—such as their timing, content quality, and engagement strategies—I can identify ways to improve medium posts. Small tweaks like better visuals, more relevant hashtags, and engaging captions can help push these posts into the high-performing category.
  
  ![Performance Categories](insta-Project/data/source_data/processed/performance_categories.png)
  ![Comparison High, Mid, Low Performing Posts](insta-Project/data/source_data/processed/Comparison_high_mid_low_performing_posts.png)
  
  ## High Performing Posts
  ![High Performance 1](insta-Project/data/source_data/processed/HPP_1.png)
  ![High Performance 2](insta-Project/data/source_data/processed/HPP_2.png)
  
  ## Medium Performing Posts
  ![Medium Performance 1](insta-Project/data/source_data/processed/MPP_1.png)
  ![Medium Performance 2](insta-Project/data/source_data/processed/MPP_2.png)
   
  ## Low Performing Posts
  ![Low Performance 1](insta-Project/data/source_data/processed/LPP_1.png)
  ![Low Performance 2](insta-Project/data/source_data/processed/LPP_2.png)

* **Image Aesthetics Analytics**:
   * Beyond captions and posting time, I explored how **visual design characteristics**—like brightness, color warmth, contrast, and saturation—relate to engagement. Each image was analyzed for its color composition and tonal qualities, then clustered into aesthetic groups.
   
   * The analysis revealed that **contrast (`std_value`)** was the most influential visual feature, meaning posts with stronger light–dark variation tended to draw more attention and interaction. This could be because such images stand out more in users’ feeds and convey depth or texture that feels visually engaging.
   
   * **Warmth (`warm_ratio`)** followed closely, suggesting that images with warmer tones—such as those featuring sunlight, warm lighting, or earthy colors—generally perform better. Warm colors often create a sense of comfort and liveliness, which may resonate more with viewers compared to colder or muted tones.
   
   * **Color intensity (`avg_saturation`)** also played a moderate role. Vibrant, saturated images seem to perform slightly better than dull ones, indicating that dynamic and vivid visuals capture user attention more effectively. However, extreme saturation may reduce authenticity, so balance matters.
   
   * **Brightness (`avg_value`)** was less predictive overall, though posts with moderate brightness tended to perform best. Overly dark or overly washed-out visuals both correlated with slightly lower engagement.
   
   * Overall, while the model’s R² score was low—indicating that aesthetics alone can’t fully explain engagement—it still highlights meaningful trends: high-performing visuals are typically **warm, contrast-rich, and moderately saturated**. This aligns with what audiences intuitively respond to in lifestyle and creative content.
   
   ![Aesthetic Feature Importances](insta-Project/data/source_data/processed/aesthetic_feature_importances.png)
   ![Aesthetic Cluster Visualization](insta-Project/data/source_data/processed/aesthetic_cluster_visualization.png)
   ![Aesthetic Cluster Visualization](insta-Project/data/source_data/processed/performance_by_aesthetic_cluster.png)
   
   ### **Summary of Model Insights**
   
   | Feature | Description | Importance |
   |----------|--------------|------------|
   | **std_value** | Brightness contrast (visual depth and variation) | 0.31 |
   | **warm_ratio** | Proportion of warm to cool tones (color temperature) | 0.24 |
   | **avg_saturation** | Color vividness or intensity | 0.21 |
   | **avg_value** | Overall brightness level | 0.19 |
   | **cluster_0–3** | Aesthetic style clusters (visual combinations) | < 0.02 |
   
   * These findings suggest that subtle visual cues—contrast, color warmth, and saturation—help shape engagement patterns, even if they don’t single-handedly predict them. Combining these insights with posting time and content strategy could improve visual consistency and audience resonance.
   
   ### **Example Visuals by Aesthetic Group**
   
   To better understand how image aesthetics relate to performance, I visualized representative samples from each cluster.
   Each group highlights distinct tonal and stylistic tendencies captured during the aesthetic clustering process.
   
   | Cluster | Aesthetic Traits | README Label | Expected File Name(s) |
   |----------|------------------|---------------|------------------------|
   | **Cluster 0** | Bright, high contrast, warm tones — lively and visually engaging. | `High Contrast Warm Tones` | `Cluster0_Sample_1.png`, `Cluster0_Sample_2.png`, `Cluster0_Sample_3.png` |
   | **Cluster 1** | Low brightness and warmth — muted, cooler palette with softer contrast. | `Low Contrast Cool Tones` | `Cluster1_Sample_1.png`, `Cluster1_Sample_2.png`, `Cluster1_Sample_3.png` |
   | **Cluster 2** | Balanced lighting, moderate saturation, neutral warmth — natural feel. | `Moderate Saturation Balanced Lighting` | `Cluster2_Sample_1.png`, `Cluster2_Sample_2.png`, `Cluster2_Sample_3.png` |
   | **Cluster 3** | Slightly higher brightness, warmer tone mix — soft, warm aesthetic. | *(optional additional group, can be skipped if redundant)* | `Cluster3_Sample_1.png`, `Cluster3_Sample_2.png`, `Cluster3_Sample_3.png` |
   
   #### **Cluster 0 — High Contrast Warm Tones**   
   Images in this cluster feature bold lighting, deep shadows, and warm highlights.  
   They stand out visually, often creating a sense of richness and texture that attracts attention.
   ![Cluster 0 - Example 1](insta-Project/data/source_data/processed/Cluster0_Sample_1.png)
   ![Cluster 0 - Example 2](insta-Project/data/source_data/processed/Cluster0_Sample_2.png)
   ![Cluster 0 - Example 3](insta-Project/data/source_data/processed/Cluster0_Sample_3.png)

   #### **Cluster 1 — Low Contrast Cool Tones**
   This group leans toward cooler, softer hues with less contrast and brightness variation.  
   It often represents a minimalist, calm aesthetic that performs steadily but not spectacularly.
   
   ![Cluster 1 - Example 1](insta-Project/data/source_data/processed/Cluster1_Sample_1.png)
   ![Cluster 1 - Example 2](insta-Project/data/source_data/processed/Cluster1_Sample_2.png)
   ![Cluster 1 - Example 3](insta-Project/data/source_data/processed/Cluster1_Sample_3.png)
   
   #### **Cluster 2 — Moderate Saturation, Balanced Lighting**
   Images here balance light and shadow well, with natural tones and moderate color intensity.  
   These visuals tend to feel realistic and approachable, aligning with mid- to high-engagement posts.
   ![Cluster 2 - Example 1](insta-Project/data/source_data/processed/Cluster2_Sample_1.png)
   ![Cluster 2 - Example 2](insta-Project/data/source_data/processed/Cluster2_Sample_2.png)
   ![Cluster 2 - Example 3](insta-Project/data/source_data/processed/Cluster2_Sample_3.png)
   
   #### **Cluster 3 — Soft Warm Mix (Optional)**
   This cluster blends slightly warm hues with gentle lighting.  
   It creates a cozy, polished look that often complements lifestyle or jewelry product shots.
   
   ![Cluster 3 - Example 1](insta-Project/data/source_data/processed/Cluster3_Sample_1.png)
   ![Cluster 3 - Example 2](insta-Project/data/source_data/processed/Cluster3_Sample_2.png)
   ![Cluster 3 - Example 3](insta-Project/data/source_data/processed/Cluster3_Sample_3.png)

---


## Suggestions & Recommendations

Based on both engagement behavior and visual aesthetic analysis, here are several actionable recommendations to improve future content performance:

### **1. Optimize Posting Time and Frequency**
   * Continue prioritizing **morning posts (8–10 AM)** when engagement peaks.
   * **Saturdays** remain the top-performing day for overall reach and interaction.  
   Supplement with **Monday or Friday** posts for consistent weekly visibility.

### **2. Strengthen Visual Composition**
   * **Increase contrast** slightly in future photos — bold light–dark separation makes visuals pop on crowded feeds.
   * Maintain **moderate saturation** levels.  
   Overly muted tones underperform, while oversaturated colors risk looking artificial.
   * **Favor warmer tones** (soft yellows, golds, or sunlit highlights).  
   These tend to elicit more emotional and aesthetic engagement.
   * Keep brightness balanced — avoid both overexposed whites and dim, underlit visuals.

### **3. Develop a Consistent Visual Identity**
   * Posts in **Cluster 0 and 2** (high contrast or balanced tones) outperformed cooler, flatter clusters.  
   Prioritize those visual styles for main feed aesthetics.
   * Use consistent color palettes and tone ratios to reinforce brand recognition.  
   This helps users instantly identify your posts within their feed.

### **4. Leverage “Saveable” Content**
   * Since **saves** are the strongest engagement predictor, focus on creating content people want to reference later:
      * Educational or informative graphics  
      * Inspirational or emotionally resonant imagery  
      * Tutorials, product context, or behind-the-scenes posts
   * Encourage saving behavior with subtle CTAs (e.g., “Save this for later”)

### **5. Elevate Medium-Performing Posts**
   * Identify visual or caption differences between **Medium** and **High** performers.  
   Usually, it’s a mix of weaker lighting, low contrast, or less engaging composition.
   * Rework older posts using the aesthetic insights:
      * Crop for focus or symmetry  
      * Adjust contrast and warmth slightly  
      * Refresh captions with context or story elements

### **6. Test and Monitor Continuously**
   * Implement **A/B testing** for:
      * Visual treatments (lighting, tone, framing)
      * Caption tone (informational vs. emotional)
      * Timing adjustments (morning vs. midday)
   * Track engagement movement per cluster group to validate visual trends over time.

### **7. Combine Visual and Behavioral Insights**
   * Engagement doesn’t depend on aesthetics alone—**timing, saves, and visual warmth together** create the strongest outcome.  
   * Build your future content calendar using both:
      * **Behavioral signals** (when and how users engage)
      * **Aesthetic signals** (what kinds of visuals they respond to)

## Future Development

While this analysis provides valuable insights, there are several avenues for future development:

1. **Content Type Analysis**:

   * Investigate which content types (e.g., images, videos, carousels) are most effective at driving engagement. Understanding which type of media resonates with users can help optimize future content. Furthermore, pushing **saves** are very important, understanding what kind of posts are saved, could be a game changer. 

2. **Granular Time Optimization**:

   * Explore specific time slots on different days of the week to see if there are even more optimal posting times than those identified in this analysis.

3. **Audience Segmentation**:

   * Delve deeper into **audience demographics** (age, gender, location) to tailor posts more effectively. This could involve creating personalized content that resonates with different segments of the audience.

4. **Hashtag Strategy**:

   * Investigate how **hashtags** affect post visibility and engagement. Experiment with different strategies for hashtag usage to identify the most effective combinations.

5. **User Feedback**:

   * Incorporate **user feedback** from comments or direct messages to gain qualitative insights into what types of content users enjoy most.

6. **A/B Testing**:

   * Use A/B testing for different **post formats**, **captions**, and **imagery** to understand what works best with the audience and refine content strategies.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---