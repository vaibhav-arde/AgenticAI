---
config:
  flowchart:
    curve: linear
---
graph TD;
	__start__([<p>__start__</p>]):::first
	start_play(start_play)
	cricket(cricket)
	badminton(badminton)
	basketball(basketball)
	__end__([<p>__end__</p>]):::last
	__start__ --> start_play;
	start_play -.-> badminton;
	start_play -.-> basketball;
	start_play -.-> cricket;
	badminton --> __end__;
	basketball --> __end__;
	cricket --> __end__;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc