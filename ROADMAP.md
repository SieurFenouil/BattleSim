# Auto Battler Game - Development Roadmap

## Project Vision 🎯
Build a web based auto battler game with automated combat mechanics and unit progression, designed for eventual transition to a web-based version. Focus on solid core mechanics and modular architecture.

## Phase 1: Core Foundation ⚡ 
**Status: In Progress** | **Target: Week 1-2**

### Combat Engine
- [x] Speed-based turn system implementation
- [x] Team vs team battle mechanics  
- [x] Basic attack and damage system
- [ ] Advanced combat actions (dodge, parry, combo)
- [ ] Buffs / Debuffs framework
- [ ] Smart selection of active moves
- [ ] Environmental effects

### Unit System
- [x] Fighter template with random stat generation
- [x] Combat entity wrapper for battle state
- [ ] Unit progression mechanics
- [ ] Acquisition of skills, passives, actives, consumables...
- [ ] Skill trees

### Interface
- [ ] Team creation
- [ ] Console logging of each turns
- [ ] Transition to Web based

### Integration & Testing
- [ ] Main game loop connecting all systems
- [ ] Sample battle scenarios for testing
- [ ] Error handling and edge case coverage
- [ ] Performance optimization for larger battles

### User Experience
- [ ] Statistics tracking and analytics

### Quality Assurance
- [ ] Comprehensive testing suite
- [ ] Performance benchmarking
- [ ] Balance testing with large datasets
- [ ] Code documentation and cleanup

### Feature Adaptation
- [ ] Convert console interface to web UI
- [ ] Implement real-time battle animations

## Technical Milestones 🛠️

### Current Sprint Goals
1. **Complete Phase 1 core systems** - Solid combat and unit mechanics
2. **Integration testing** - Ensure all components work together seamlessly  
3. **Performance baseline** - Establish benchmarks for future optimization

### Key Decision Points
- **Unit balance**: Finalize stat ranges and progression curves
- **Combat complexity**: Determine optimal number of actions/mechanics
- **Web timing**: When to start web transition planning

### Success Metrics
- **Stability**: Zero crashes during extended play sessions
- **Balance**: No single strategy dominates all others  
- **Performance**: Battles complete in reasonable time even with many units
- **Modularity**: Easy to add new features without major refactoring

---

**Last Updated**: Current session  
**Next Review**: After Phase 1 completion